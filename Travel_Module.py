################################################################################
##
## Filename: Travel_Module.py
## Purpose: Defines frequently used functions for the travel project
## Author: Laura Kaufmann
##
################################################################################

#===============================================
# Connecting to the essential datasets
#===============================================

## Defines geodatabase location; to be used in all scripts
def getGDBconnection():
  import os
  db_loc = r"C:\Users\Laura\AppData\Roaming\Esri\ArcGISPro\Favorites\Travel_PROD.sde"
  db_name = r"Travel_PROD.DBO"
  db_path = os.path.join(db_loc, db_name)
  return [db_loc, db_name, db_path]

def getESRICountries():
  url = r"https://services.arcgis.com/P3ePLMYs2RVChkJx/arcgis/rest/services/World_Countries/FeatureServer/0"
  fields = ["COUNTRY", "ISO_CC", "CONTINENT", "COUNTRYAFF"]
  return [url, fields]

#===============================================
# Working with geodatabases
#===============================================

## Lookup values from the database table and field
def lookupFieldValues(workspace, table, field, where_qry=None):
    import os
    import arcpy
    table_path = os.path.join(workspace[0],table)

    with arcpy.da.SearchCursor(table_path, [field], where_clause=(where_qry)) as cursor:
        return sorted({row[0] for row in cursor})

## Get values from a specified domain
def getDomainValues(domainName):
  import arcpy
  workspace = getGDBconnection()

  domains = arcpy.da.ListDomains(workspace[0])
  domainValues = []

  for domain in domains:
    if domain.name == domainName:
      coded_values = domain.codedValues
      for val, desc in coded_values.items():
        domainValues.append(str(val))

  return domainValues

#===============================================
# Working with time stamps
#===============================================

## Get today's date
def getTodayDate():
  import datetime as dt
  return dt.datetime.now()

## Format an input date for inclusion in file names
def formatFileDate(in_date):
  return in_date.strftime("%Y_%m_%d")