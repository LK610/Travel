################################################################################
##
## Filename: RegionalMapping.py
## Purpose: Update Trip polygons
## Author: Laura Kaufmann
##
################################################################################

# Import and connect

## Import packages
import Travel_Module as tm
import arcpy
import os

## Define workspaces
db_connect = tm.getGDBconnection()
arcpy.env.overwriteOutput = True
arcpy.env.workspace = db_connect[0]
scratchWorkspace = r"C:\Users\Laura\Documents\Keepsakes\Travel\1_RegionalMapping"

## Define the output file name
file_date = tm.formatFileDate(tm.getTodayDate())
file_name = str("Trip_Overview_" + file_date + ".pdf")
file_path = os.path.join(scratchWorkspace, file_name)

## Connect to database
regions = db_connect[2] + "\Regions"
trips = db_connect[2] + "\Trips"
worldhex = db_connect[2] + "\WorldHex"

euro_poly_fc_name = scratchWorkspace + "\Dissolved_Trips"

## Print initial check
#arcpy.AddMessage("Workspaces and variables defined...")
print("Workspaces and variables defined...")

# Create layer of dissolved hexagons

try:
    ## Select features where Trip_ID <> "000"
    hex_europe = arcpy.management.SelectLayerByAttribute(worldhex, "NEW_SELECTION", "Trip_ID <> '000'", None)

    ## Generate merged shapes based on the Trip_ID
    dissolved_trips = arcpy.analysis.PairwiseDissolve(hex_europe, euro_poly_fc_name, ["Trip_ID"], "", "MULTI_PART")
    
    arcpy.AddMessage("WorldHex features dissolved...")
    
except:
    arcpy.AddMessage("Something went wrong dissolving WorldHex features. Please check the script.")