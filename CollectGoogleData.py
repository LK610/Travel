# Test variables
#url = r"https://www.google.com/maps/place/Trinity+College/@52.2069577,0.1130816,17z/data=!3m1!4b1!4m5!3m4!1s0x47d870bbe0dcd367:0xe841058978d4a675!8m2!3d52.2069577!4d0.1130816"
#url = r"https://www.google.com/maps/place/Uffizi+Gallery/@43.7677856,11.2553108,17z/data=!3m1!4b1!4m5!3m4!1s0x132a54008dc59081:0xcddeb7c89bf0c4cd!8m2!3d43.7677856!4d11.2553108"
#url = r"https://www.google.com/maps/place/Ny+Carlsberg+Glyptotek/@55.67298,12.572543,17z/data=!3m1!4b1!4m5!3m4!1s0x465253130411747d:0x599f2e4fe338e7a1!8m2!3d55.67298!4d12.572543"
#url = r"https://www.google.com/maps/place/King%E2%80%99s+Cross/@51.5348485,-0.1299922,16z/data=!4m13!1m7!3m6!1s0x48761b10c73c4dcd:0x616f11fed05d6bb9!2sKings+Cross,+London,+UK!3b1!8m2!3d51.5347488!4d-0.1245845!3m4!1s0x48761b3c5cbf139b:0x7be9c9cf71db38fb!8m2!3d51.5317236!4d-0.1246057"
#url = r"https://www.google.com/maps/place/Restaurant+Tradition/@59.3259554,18.0716646,17z/data=!3m1!4b1!4m5!3m4!1s0x465f9d6ea9aaaaab:0xa4841fc300c6afe2!8m2!3d59.3260004!4d18.0738143"
#url = r"https://www.google.com/maps/place/Rome,+Metropolitan+City+of+Rome+Capital,+Italy/@41.9102415,12.3959149,11z/data=!3m1!4b1!4m6!3m5!1s0x132f6196f9928ebb:0xb90f770693656e38!8m2!3d41.9027835!4d12.4963655!16zL20vMDZjNjI"
url = r"https://www.google.com/maps/place/France/@46.1390308,-2.435177,6z/data=!3m1!4b1!4m6!3m5!1s0xd54a02933785731:0x6bfd3f96c747d9f7!8m2!3d46.227638!4d2.213749!16zL20vMGY4bDlj"

# Import necessary packages
import arcpy
import Travel_Module as tm

from selenium import webdriver
from selenium.webdriver.common.by import By

# Define functions
def getElement(browser, xpath, attribute):
    try:
        element = browser.find_element_by_xpath(xpath).get_attribute(attribute).strip()

        if len(element) == 0:
            return ""
        else:
            return(element)

    except:
        return ""

def createPoint(url):
    # Get coordinates from URL
    coords = url.split("/@")
    coords = coords[1].split(",17z")[0]
    coords = coords.split(",")

    lat = coords[0]
    lon = coords[1]

def scrapeURL(url):
    # Set up Chrome driver
    driver_path = r"C:\chromedriver.exe"
    browser = webdriver.Chrome(driver_path)
    browser.get(url)

    # Get variables
    name = getElement(browser, '//*[contains(@class, "DUwDvf")]', "innerText")

    if len(getElement(browser, '//*[contains(@class, "bwoZTb")]', "innerText")) == 0:
        localname = getElement(browser, '//*[contains(@class, "DUwDvf")]', "innerText")
    else:
        localname = getElement(browser, '//*[contains(@class, "bwoZTb")]', "innerText")

    imglink = getElement(browser, '//*[contains(@class, "aoRNLd")]//img[1]', "src")
    desc = getElement(browser, '//*[contains(@class, "PYvSYb")]', "innerText") #"wEvh0b"

    type = getElement(browser, '//*[contains(@class, "DkEaL u6ijk")]', "innerText")
    website = getElement(browser, '//*[contains(@data-item-id, "authority")]', "href")
    address = getElement(browser, '//*[contains(@data-item-id, "address")]', "innerText")
    phone = getElement(browser, '//*[contains(@data-item-id, "phone")]', "innerText")

    browser.quit()

    # Print results
    print(name)
    print(localname)
    print(imglink)
    print(type)
    print(desc) 
    print(website)
    print(address)
    print(phone)

scrapeURL(url)

#Region_ID	
#Location_ID	
#LOC_Category	
#LOC_Type	
#LOC_Name = name
#LOC_LocalName = localname
#LOC_Desc = desc
#LOC_Website = website
#LOC_Address = address
#LOC_Phone = phone
#LOC_ImgLink = imglink
#LOC_Interest = "Low"
#Latitude
#Longitude

