################################################################################
##
## Filename: WebScrapping.py
## Purpose: Defines functions used to scrape websites for travel data
## Author: Laura Kaufmann
##
################################################################################

#===============================================
# Base functions
#===============================================

# Get the element at a relative xpath and attribute, returns empty string on failure
def getElement(browser, xpath, attribute):
    try:
        element = browser.find_element_by_xpath(xpath).get_attribute(attribute).strip()

        if len(element) == 0:
            return ""
        else:
            return(element)

    except:
        return ""

# Scrape a Google Maps URL to return latitude and longitude as a list
def findCoordinates(url):
    coords = url.split("/@")
    coords = coords[1].split(",17z")[0]
    coords = coords.split(",")
    return coords

    #lat = coords[0]
    #lon = coords[1]

#===============================================
# Find specific elements on Google Maps pages
#===============================================

def getName(browser):
    return getElement(browser, '//*[contains(@class, "DUwDvf")]', "innerText")

def getLocalName(browser):
    
    localname = getElement(browser, '//*[contains(@class, "DUwDvf")]', "innerText")
    
    if len(localname) == 0:
            return getName(browser)
    else:
        return localname

def getImageLink(browser):
    return getElement(browser, '//*[contains(@class, "aoRNLd")]//img[1]', "src")

def getSimpleDesc(browser):
    return getElement(browser, '//*[contains(@class, "PYvSYb")]', "innerText")

def getLocationType(browser):
    return getElement(browser, '//*[contains(@class, "DkEaL u6ijk")]', "innerText")

def getAddress(browser):
    return getElement(browser, '//*[contains(@data-item-id, "address")]', "innerText")

def getPhone(browser):
    return getElement(browser, '//*[contains(@data-item-id, "phone")]', "innerText")

#===============================================
# Find specific elements on TimeandDate.com pages
#===============================================
#https://www.timeanddate.com/time/zone/sweden

#===============================================
# Find specific elements on State Department pages
#===============================================
#https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Denmark.html