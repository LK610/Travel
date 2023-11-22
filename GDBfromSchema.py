################################################################################
## Filename: GDBfromSchema.py
## Purpose: Create an empty file geodatabase from an Excel template
## Author: Laura Kaufmann
################################################################################

# IMPORT PACKAGES
import arcpy
from arcpy import metadata as md

import os
import pandas as pd

import logging
logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# ABOUT THE TARGET GEODATABASE
sr = arcpy.SpatialReference(4326)

fldr = r"C:\Users\Laura\Documents\Keepsakes\Travel\0_MetadataInstructions\2022 Database Migration"
name = r"Travel_Archive"
gdb = name + ".gdb"

# READ IN THE TEMPLATE SPREADSHEET
xlsx_fldr = r"C:\Users\Laura\Documents\Keepsakes\Travel\0_MetadataInstructions"
xlsx_file = r"Data_Dictionary.xlsx"
xlsx = os.path.join(xlsx_fldr, xlsx_file)

# METADATA VARIABLES
credits = "Schema designed and data populated by Laura Kaufmann (lmmk81914@gmail.com)"
constraints = "Data and schema can only be used with writted permission from Laura Kaufmann (lmmk81914@gmail.com)"

# FOLDER OF SQL TXT FILES FOR VIEWS
sqlFldr = r"C:\Users\Laura\Documents\Keepsakes\Travel\0_MetadataInstructions\ViewSQL"

# FUNCTIONS
def getValue(argument):
    if argument == 'NONE':
        return None
    else:
        return argument

logging.info('Packages imported; ready to begin')

# DELETE AND CREATE THE TARGET GEODATABASE
arcpy.management.Delete(os.path.join(fldr, gdb), '')
arcpy.management.CreateFileGDB(fldr, name, "CURRENT")

wrkspc = os.path.join(fldr, gdb)
arcpy.env.overwriteOutput = True

logging.info('Blank file geodatabase created')

# CREATE DOMAINS AND ADD VALUES
domains = pd.read_excel(xlsx, sheet_name='Domains')
domainValues = pd.read_excel(xlsx, sheet_name='DomainValues')

for index, row in domains.iterrows():
    domain_name = row['Name']
    domain_description = row['Description']
    field_type = row['FieldType']
    domain_type = row['DomainType']
    split_policy = row['SplitPolicy']
    merge_policy = row['MergePolicy']

    ##https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-domain.htm
    arcpy.management.CreateDomain(wrkspc, domain_name, domain_description, field_type, domain_type, split_policy, merge_policy)
        
    for index, row in domainValues.iterrows():
        if row['Name'] == domain_name:
            if domain_type == 'CODED':
                ##https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-coded-value-to-domain.htm
                arcpy.management.AddCodedValueToDomain(wrkspc, domain_name, row['Code'], row['ValueDescription'])
            else:
                ##https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/set-value-for-range-domain.htm
                arcpy.management.SetValueForRangeDomain(wrkspc, domain_name, row['MinValue'], row['MaxValue'])

    logging.info('%s domain and values added to the geodatabase', domain_name)

# CREATE TABLES
tables = pd.read_excel(xlsx, sheet_name='Tables')
tables = tables.fillna('NONE')

fields = pd.read_excel(xlsx, sheet_name='Fields')
fields = fields.fillna('NONE')

for index, row in tables.iterrows():
    
    out_name = row['Name']
    geometry_type = row['Geometry']
    has_m = row['HasM']
    has_z = row['HasZ']
    summary = row['TableDefinition']
    
    if row['Module'] == 'None':
        tag = geometry_type.capitalize()
    else:
        tag = "{}, {}".format(row['Module'], geometry_type.capitalize())
        
    if geometry_type == 'TABLE':
        ##https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-table.htm
        arcpy.management.CreateTable(wrkspc, out_name, None, '', '')
        logging.info('%s table created in the geodatabase', out_name)
    else:
        ##https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-feature-class.htm
        arcpy.management.CreateFeatureclass(wrkspc, out_name, geometry_type, None, has_m, has_z, sr)
        logging.info('%s feature class created in the geodatabase', out_name)
    
    mdDesc = []
    
    for index, row in fields.iterrows():
        if row['Table'] == out_name:
            
            field_name = getValue(row['FieldName'])
            field_type = getValue(row['FieldType'])
            field_precision = getValue(row['Precision'])
            field_scale = getValue(row['Scale'])
            field_length = getValue(row['Length'])
            field_alias = getValue(row['FieldAlias'])
            field_is_nullable = getValue(row['Nullable'])
            field_is_required = getValue(row['Required'])
            field_domain = getValue(row['FieldDomain'])
            field_default = getValue(row['DefaultValue'])
            
            ##https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/add-field.htm
            arcpy.management.AddField(os.path.join(wrkspc, out_name), field_name, field_type, field_precision, field_scale, field_length, field_alias, field_is_nullable, field_is_required, field_domain)
            
            if field_default != None:
                ##https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/assign-default-to-field.htm
                arcpy.management.AssignDefaultToField(os.path.join(wrkspc, out_name), field_name, field_default)
                setDesc = " (Default: {})".format(field_default)
            
            if field_domain != None:
                setDesc = " ({})".format(field_domain)
            
            if field_default != None and field_domain != None:
                setDesc = " (Default: {} ({}))".format(field_default, field_domain)
            else:
                setDesc = ""
            
            fieldDesc = "{} ({}) - {}{}".format(field_name, field_type.capitalize(), row['FieldDefinition'], setDesc)
            mdDesc.append(fieldDesc)
            
    logging.info('Fields added to %s', out_name)
    
    ##https://pro.arcgis.com/en/pro-app/latest/arcpy/metadata/metadata-class.htm
    new_md = md.Metadata()
    new_md.title = out_name
    new_md.tags = tag
    new_md.summary = summary
    new_md.description = '\n'.join(mdDesc)
    new_md.credits = credits
    new_md.accessConstraints = constraints
    
    tgt_item_md = md.Metadata(os.path.join(wrkspc, out_name))
    if not tgt_item_md.isReadOnly:
        tgt_item_md.copy(new_md)
        tgt_item_md.save()