################################################################################
## Filename: RegionalMapping.py
## Purpose: Update Trip polygons
## Author: Laura Kaufmann
################################################################################

# Import packages, define workspaces, define variables

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
regions = db_connect[2] + ".Regions"
trips = db_connect[2] + ".Trips"
worldhex = db_connect[2] + ".WorldHex15000"

interim_fc_name = scratchWorkspace + r"\New_Trips"

## Print initial check
#arcpy.AddMessage("Workspaces and variables defined...")
print("Workspaces and variables defined...")

# Populate the New Trips feature class with the most current geometries

## Dissolve hexagons to generate Europe trips
try:
    ### Select features where Trip_ID <> "000"
    hex_europe = arcpy.management.SelectLayerByAttribute(worldhex, "NEW_SELECTION", "Trip_ID <> '000'", None)

    ### Generate merged shapes based on the Trip_ID
    dissolved_trips = arcpy.analysis.PairwiseDissolve(hex_europe, interim_fc_name, ["Trip_ID"], "", "MULTI_PART")
    
    arcpy.AddMessage("WorldHex features dissolved...")
    
except:
    arcpy.AddMessage("Something went wrong dissolving WorldHex features. Please check the script.")

## Calculate minimum bounding geometry for all other trips

### Generate bounding geometries for all trips
#other_fc_name = scratchWorkspace + r"\all_other_trips"
#arcpy.management.MinimumBoundingGeometry("Travel_PROD.DBO.Regions", other_fc_name, "CONVEX_HULL", "LIST", "Trip_ID", "NO_MBG_FIELDS")

### Get list of other trips
other_trip_ids = []
other_qry = "Trip_Type <> 'Europe'"
with arcpy.da.SearchCursor(trips,["Trip_ID"],other_qry) as other_search:
        for row in other_search:
            other_trip_ids.append(row[0])

print(other_trip_ids)