import Travel_Module as tm
import WebScrapping as ws
import arcpy

from selenium import webdriver
from selenium.webdriver.common.by import By

#------
trip_title = 'Low Countries Train Tour'
currency_values = tm.getDomainValues("Currency")
print(currency_values)

#------

# Pyuic trouble shooting
#     1. Typed the command into the windows powershell
#     2. Typed the command into the 
#     uninstalled and reinstalled PyQT5 via 
#     Created a bat file and added the location of to the environment system variable PATH (https://stackoverflow.com/questions/41381660/pyqt5-pyuic-module-error)

 # Set up Chrome driver
driver_path = r"C:\chromedriver.exe"
browser = webdriver.Chrome(driver_path)
browser.get(url)

    # Update Region Name (le_reg_Name)
print(ws.getName(browser))
    # Update Local Name (le_reg_LocalName)
print(ws.getName(browser))
    # Update Region Description (txt_reg_description)
    # Update Image Link URL text (txt_reg_ImgURL)
    # Display the image in the GUI (vw_reg_ImgDisplay)
    # Update Latitude (dspin_reg_Latitude)
    # Update Longitude (ddspin_reg_Longitude)

browser.quit()