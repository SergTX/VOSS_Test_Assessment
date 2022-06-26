import requests
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig as rc
from utilities.loggerCustom import Logging

baseURl = rc.purchase_url()
loggerr = Logging.logging()

@pytest.mark.regression
@pytest.mark.jenkins
@allure.severity(allure.severity_level.NORMAL)
def test_checkLinks(setup):
    loggerr.info("************ Test 007 - Start  **************")
    global response
    bad_url = 0
    btw = 0
    good_url = 0
    driver = setup
    loggerr.info("************ Open Browser **************")
    driver.get(baseURl)
    driver.implicitly_wait(10)
    driver.maximize_window()
    loggerr.info("************ Collecting all links  **************")
    allLinks = driver.find_elements(By.TAG_NAME, "a")
    print(f"Total number of links on website : ", len(allLinks))
    loggerr.info("************ Checking response code of all links  **************")
    for link in allLinks:
        url = link.get_attribute('href')
        try:
            response = requests.head(url)
        except:
            None
        if response.status_code >= 400:
            bad_url+=1
            print('This url is bad', url , response.status_code)
        elif response.status_code>=300:
            btw+=1
            print(f'Response code between 300 and 400', url, response.status_code)
        else:
            good_url += 1
            print(f'This a good url:', url, response.status_code)
    loggerr.info("************ Closing browser **************")
    driver.close()
    print(f'Total number of good links is :', good_url)
    print(f'Total number of 3xx responses is :', btw)
    print(f'Total number of bad links is :', bad_url)
    loggerr.info("************ Test 007 - End  **************")