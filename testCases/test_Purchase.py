# #  Step 6 . browser to "Fake pricing page" and purchase basic package
import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig as rc
from utilities.customLogger import LogGen

baseURl = rc.purchase_url()
loggerr = LogGen.loggen()


@pytest.mark.smoke
@pytest.mark.regression
@allure.severity(allure.severity_level.NORMAL)
def test_Purchase_basicPackage(setup):
    loggerr.info("************ Test 005 - Start  **************")
    loggerr.info("************ Open Browser **************")
    driver = setup
    driver.get(baseURl)
    driver.implicitly_wait(10)
    driver.maximize_window()

    #navigate to "Fake pricing page"
    loggerr.info("************ Navigate to Automation Exersises  **************")
    link_to_auto_page = driver.find_element(By.LINK_TEXT, 'Automation Exercises')
    link_to_auto_page.click()
    time.sleep(2)
    loggerr.info("************ Navigate to Fake Pricing Page  **************")
    link_to_fake_page = driver.find_element(By.LINK_TEXT, 'Fake Pricing Page')
    link_to_fake_page.click()

    loggerr.info("************ Scroll down on 300 px  **************")
    # scroll down
    time.sleep(2)
    driver.execute_script("window.scrollTo(0,300)")

    # clicking on purchase Basic package
    time.sleep(2)
    loggerr.info("************ Clicking on Basic Package Purchase  **************")
    purchase_basic = driver.find_element(By.XPATH, '//*[@id="post-5050"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div/div/div[4]/a')
    purchase_basic.click()
    loggerr.info("************ Closing browser **************")
    driver.close()
    loggerr.info("************ Test 005 - End  **************")
