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

logging.info('Packages imported; ready to begin')

# DELETE AND CREATE THE TARGET GEODATABASE
arcpy.management.Delete(os.path.join(fldr, gdb), '')
arcpy.management.CreateFileGDB(fldr, name, "CURRENT")

wrkspc = os.path.join(fldr, gdb)
arcpy.env.overwriteOutput = True

logging.info('Blank file geodatabase created')

# CREATE TABLES
tables = pd.read_excel(xlsx, sheet_name='Tables')

for index, row in tables.iterrows():

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
    
    logging.info('%s table created in the geodatabase', out_name)

# CREATE DOMAINS
domains = pd.read_excel(xlsx, sheet_name='Domains')

for index, row in domains.iterrows():

    domain_name = row['Name']
    domain_description = row['Description']
    field_type = row['FieldType']
    domain_type = row['DomainType']
    split_policy = row['SplitPolicy']
    merge_policy = row['MergePolicy']

    arcpy.management.CreateDomain(wrkspc, domain_name, domain_description, field_type, domain_type, split_policy, merge_policy)
    logging.info('%s domain created in the geodatabase', domain_name)

# CREATE DOMAIN VALUES
domainValues = pd.read_excel(xlsx, sheet_name='DomainValues')
domainValues = domainValues.merge(domains, how='inner')

uniqueDomains = domainValues.Name.unique().tolist()

for u in uniqueDomains:
    for index, row in domainValues.iterrows():
        if row['Name'] == u:
            if row['DomainType'] == 'CODED':
                arcpy.management.AddCodedValueToDomain(wrkspc, u, row['Code'], row['ValueDescription'])
            else:
                arcpy.management.SetValueForRangeDomain(wrkspc, u, row['MinValue'], row['MaxValue'])
        else:
            pass

    logging.info('%s domain values added in the geodatabase', u)