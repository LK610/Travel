## Print all conda environments
#C:\Users\Laura\anaconda3\Scripts\conda.exe info --envs

## Set conda environment
#C:/Users/Laura/anaconda3/Scripts/activate "C:\Users\Laura\Documents\Envs\Python envs\arcgispro-py3-clone"

## Convert ui to Python file
#"C:\Users\Laura\Documents\Envs\Python envs\arcgispro-py3-clone\python.exe" –m PyQt5.uic.pyuic "C:\AttributeEditor.ui" –o AttributeEditor_ui.py
#"C:\Users\Laura\Documents\Envs\Python envs\arcgispro-py3-clone\python.exe" –m PyQt5.uic.pyuic "C:\AttributeEditor.ui" –o "C:\AttributeEditor_ui.py"

# https://www.e-education.psu.edu/geog489/l2_p5.html
# https://www.e-education.psu.edu/geog489/node/2226
# https://tereshenkov.wordpress.com/2017/11/26/developing-python-gui-in-arcgis-pro-with-pyqt/
# https://stackoverflow.com/questions/41381660/pyqt5-pyuic-module-error

#* Important 
#! Alert
#? Question
# TODO

#===============================================
# Import required resources
#===============================================

# Import packages
import sys
 
from PyQt5.QtWidgets import QApplication, QMainWindow, QStyle, QFileDialog, QMessageBox
try:
    from PyQt5.QtWebEngineWidgets import QWebEngineView as WebMapWidget
except:
    from PyQt5.QtWebKitWidgets import QWebView as WebMapWidget

from selenium import webdriver
from selenium.webdriver.common.by import By

# Import other Python modules
import AttributeEditor_ui as ui
import Travel_Module as tm
import WebScrapping as ws

#===============================================
# GUI event handler and related functions 
#===============================================

# Get Trip_ID from combo box in header
def changeTrip_ID():
    # Change label text in the header (lbl_Trip_ID)
    title = ui.combo_Trip_Name.currentText()
    trip_id = tm.lookupFieldValues(tm.getGDBconnection(), "Travel_PROD.DBO.LOC_Trips", "Trip_ID", "Trip_Title = '{0}'".format(title))
    ui.lbl_Trip_ID.setText(trip_id)
    
    # Change Region_ID prefix (le_reg_RegionID)
    ui.le_reg_RegionID.setText(trip_id)

    # Change combo box options in combo_loc_Name
    regions = tm.lookupFieldValues(tm.getGDBconnection(), "Travel_PROD.DBO.LOC_Regions", "REG_Name", "Trip_ID = '{0}'".format(trip_id))
    ui.combo_loc_RegName.addItems(regions)

# Region
## Get Region data from a Google Maps URL (btn_reg_getURLdata)
def getRegionData(url):

    # Set up Chrome driver
    driver_path = r"C:\chromedriver.exe"
    browser = webdriver.Chrome(driver_path)
    browser.get(url)

    # Update Region Name (le_reg_Name)
    ui.le_reg_Name.setText(ws.getName(browser))
    # Update Local Name (le_reg_LocalName)
    ui.le_reg_Name.setText(ws.getName(browser))
    # Update Region Description (txt_reg_description)
    # Update Image Link URL text (txt_reg_ImgURL)
    # Display the image in the GUI (vw_reg_ImgDisplay)
    # Update Latitude (dspin_reg_Latitude)
    # Update Longitude (ddspin_reg_Longitude)

    browser.quit()
    return ""

## Add user-verified Region data to the database (btn_reg_AddtoDatabase)
def addRegion():
    return ""

# Countries
## (btn_cntry_FindCountries)
## (btn_cntry_AddCountry)

# Location
## (btn_loc_getURLdata)
## (btn_loc_AddtoDatabase)

# Function to parse coordinates from the Google Maps URL
def createPoint(url):
    coords = url.split("/@")
    coords = coords[1].split(",17z")[0]
    coords = coords.split(",")
    return coords

# Function to find an element on the Google Maps page
def getElement(browser, xpath, attribute):
    try:
        element = browser.find_element_by_xpath(xpath).get_attribute(attribute).strip()

        if len(element) == 0:
            return ""
        else:
            return(element)

    except:
        return ""

#===============================================
# create app and main window + dialog GUI 
#===============================================
# app = QApplication(sys.argv) 
 
# # set up main window 
# mainWindow = QMainWindow() 
# ui = gui_main.Ui_MainWindow() 
# ui.setupUi(mainWindow) 

# On load, import values for comboboxes
trip_titles = tm.lookupFieldValues(tm.getGDBconnection(), "Travel_PROD.DBO.LOC_Trips", "Trip_Title", "Trip_Stage <> 'Complete'")
ui.combo_Trip_Name.addItems(trip_titles)

## Region
ui.combo_reg_Interest.addItems(tm.getDomainValues("Interest"))
ui.combo_reg_Interest.setCurrentText("Low")

ui.combo_reg_DayTrip.addItems(tm.getDomainValues("YesNoNAUnk"))
ui.combo_reg_DayTrip.setCurrentText("No")

## Countries
ui.combo_cntry_Currency.addItems(tm.getDomainValues("Currency"))
ui.combo_cntry_Currency.setCurrentText("EUR")

## Location
#category_values = tm.getDomainValues("??")
#ui.combo_loc_Category.addItems(category_values)

#===============================================
# connect signals 
#===============================================

# Trip combo box in header
ui.combo_Trip_Name.currentTextChanged.connect(changeTrip_ID())

#===============================================
# initialize global variables 
#===============================================



#===============================================
# test availability and if run as script tool 
#===============================================
# arcpyAvailable = core_functions.importArcpyIfAvailable() 
 
# if not arcpyAvailable: 
#     ui.statusbar.showMessage('arcpy not available. Adding to shapefiles and layers has been disabled.') 

#===============================================
# run app 
#===============================================
# mainWindow.show() 
# sys.exit(app.exec_()) 