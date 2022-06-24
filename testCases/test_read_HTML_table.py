
# print table extract date from html table

from selenium import webdriver
import time
import allure
import pytest
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig as rc
from utilities.loggerCustom import Logging
from pageObjects.FillFormsPage import Fill_forms
from pageObjects.HTML_el_page import HTML_table
import sys
from datetime import datetime
from utilities.time_stamp import *

baseUrl = rc.baseUrl()
loggerr = Logging.logging()


@pytest.mark.smoke
@pytest.mark.regression
def test_read_htmlTable(setup):
    sys.stdout = open("..//Reports/ResultsHtmlTable.txt", "a")
    loggerr.info("************ Test 008 - Start  **************")
    rows_path = rc.rows_table()
    cols_path = rc.cols_table()
    loggerr.info("************ Open Browser **************")
    driver = setup
    driver.get(baseUrl)
    driver.implicitly_wait(10)
    driver.maximize_window()

    ht= HTML_table(driver)
    time.sleep(2)
    loggerr.info("************ Click on Automation Exercises  **************")
    ht.goToAutomate()
    time.sleep(2)
    loggerr.info("************ Click on Interactions with simple elements **************")
    ht.goTo_Elemenets()
    time.sleep(2)
    loggerr.info("************ Scroll down **************")
    ht.scroll_down()

    #  count rows and columns of the html table with id
    loggerr.info("************ Collecting and counting Rows and Columns **************")
    rows = len(driver.find_elements(By.XPATH, rows_path))
    cols = len(driver.find_elements(By.XPATH, cols_path))
    driver.save_screenshot("..//Screenshots//" + "Capture HTML Table.png")
    print("\n                        HTML TABLE INFO   " ,   date)
    print(f"\n Table contains number of rows :" , rows)
    print(f"\n Table contains number of columns :", cols,"\n")

    # reading data from table ( pick title and work)
    loggerr.info("************ Reading Data from HTML Table **************")
    for r in range(2,rows+1):
        for c in range(1,cols+1):
            data = driver.find_element(By.XPATH,"//table[contains(@id,'htmlTableId')]/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
            print(data,end="            ")
        print()
    loggerr.info("************ Printing Data  **************")
    loggerr.info("************ Closing browser **************")
    ht.close_driver()
    loggerr.info("************ Test 008 - End  **************")
    time.sleep(2)
    sys.stdout.close()
    sys.stdout = sys.__stdout__

