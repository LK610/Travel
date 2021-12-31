################################################################################
##
## Filename: Travel_Module.py
## Purpose: Defines frequently used functions for the travel project
## Author: Laura Kaufmann
##
################################################################################

# Connecting to the Travel_PROD database
## Defines geodatabase location; to be used in all scripts
def getGDBconnection():
  import os
  db_loc = r"C:\Users\Laura\AppData\Roaming\Esri\ArcGISPro\Favorites\Travel_PROD.sde"
  db_name = r"Travel_PROD.DBO"
  db_path = os.path.join(db_loc, db_name)
  return [db_loc, db_name, db_path]

# Working with time stamps
## Get today's date
def getTodayDate():
  import datetime as dt
  return dt.datetime.now()

## Format an input date for inclusion in file names
def formatFileDate(in_date):
  return in_date.strftime("%Y_%m_%d")

# ???
#def compare_geometry():
#  return "IDK"