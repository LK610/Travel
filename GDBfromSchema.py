################################################################################
## Filename: GDBfromSchema.py
## Purpose: Create an empty file geodatabase from an Excel template
## Author: Laura Kaufmann
################################################################################

# IMPORT PACKAGES
import arcpy

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

# FOLDER OF SQL TXT FILES FOR VIEWS
sqlFldr = r"C:\Users\Laura\Documents\Keepsakes\Travel\0_MetadataInstructions\ViewSQL"

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
## Create feature class: https://pro.arcgis.com/en/pro-app/latest/tool-reference/data-management/create-feature-class.htm
tables = pd.read_excel(xlsx, sheet_name='Tables')
print(tables)

"""for index, row in tables.iterrows():

    out_name = row['Name']
    geometry_type = row['Geometry']
    has_m = row['HasM']
    has_z = row['HasZ']

    if geometry_type == 'TABLE':
        arcpy.management.CreateTable(wrkspc, out_name, None, '', '')
        logging.info('%s table created in the geodatabase', out_name)
    else:
        arcpy.management.CreateFeatureclass(wrkspc, out_name, geometry_type, None, has_m, has_z, sr)
        logging.info('%s feature class created in the geodatabase', out_name)
    
    logging.info('%s table created in the geodatabase', out_name)"""

