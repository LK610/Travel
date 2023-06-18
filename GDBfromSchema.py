################################################################################
## Filename: GDBfromSchema.py
## Purpose: Create an empty file geodatabase from an Excel template
## Author: Laura Kaufmann
################################################################################

# IMPORT PACKAGES
import arcpy
import os
import pandas as pd

# ABOUT THE TARGET GEODATABASE
sr = arcpy.SpatialReference(4326)

fldr = r"C:\Users\Laura\Documents\Keepsakes\Travel\0_MetadataInstructions\2022 Database Migration"
gdb = r"Travel_Archive.gdb"
wrkspc = os.path.join(fldr, gdb)

arcpy.env.overwriteOutput = True

# READ IN THE TEMPLATE SPREADSHEET
xlsx_fldr = r"C:\Users\Laura\Documents\Keepsakes\Travel\0_MetadataInstructions"
xlsx_file = r"Data_Dictionary.xlsx"
xlsx = os.path.join(xlsx_fldr, xlsx_file)

# CREATE TABLES
tables = pd.read_excel(xlsx, sheet_name='Tables')

for index, row in tables.iterrows():

    out_name = row['Name']
    geometry_type = row['Geometry']
    has_m = row['HasM']
    has_z = row['HasZ']

    if geometry_type == 'TABLE':
        arcpy.management.CreateTable(wrkspc, out_name, None, '', '')
    else:
        arcpy.management.CreateFeatureclass(wrkspc, out_name, geometry_type, None, has_m, has_z, sr)