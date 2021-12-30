################################################################################
##
## Filename: RegionalMapping.py
## Purpose: Update Trip polygons
## Author: Laura Kaufmann
##
################################################################################

# Import and connect

## Import packages
import arcpy
import os
import datetime as dt
import Travel_Module

## Define workspaces
db_location = Travel_Module.getGDBlocation
arcpy.env.overwriteOutput = True
arcpy.env.workspace = db_location

print(db_location)