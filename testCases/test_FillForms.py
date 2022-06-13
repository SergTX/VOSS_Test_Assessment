# Step 5. Browse to Fill out Forms page and complete all forms , followed by submit actions

import time
import allure
import pytest
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig as rc
from utilities.customLogger import LogGen
from pageObjects.FillFormsPage import Fill_forms

class Test_Fillforms:

    loggerr = LogGen.loggen()
    baseUrl = rc.baseUrl()

    L_name = rc.L_name()
    L_message = rc.L_message()
    R_name = rc.R_name()
    R_message = rc.R_message()


    @pytest.mark.regression
    @allure.severity(allure.severity_level.NORMAL)
    def test_fill_the_forms(self, setup):
        self.loggerr.info("************ Test 004 - Start  **************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.loggerr.info("************ Open Browser **************")
        time.sleep(1)

        self.loggerr.info("************ Navigate to Automation Exersises  **************")
        self.link_to_auto_page = self.driver.find_element(By.LINK_TEXT, 'Automation Exercises')
        self.link_to_auto_page.click()
        time.sleep(1)

        self.loggerr.info("************ Navigate to Fill Out Forms  **************")
        link_to_fillout_page = self.driver.find_element(By.LINK_TEXT, 'Fill out forms')
        link_to_fillout_page.click()

        self.loggerr.info("************ Entering Left name  **************")
        self.ff = Fill_forms(self.driver)
        self.ff.typeLeftName(self.L_name)
        time.sleep(1)

        self.loggerr.info("************ Entering Left message  **************")
        self.ff.typeLeftMessage(self.L_message)
        time.sleep(3)

        self.loggerr.info("************ Left Submit click  **************")
        self.ff.L_submit_click()
        time.sleep(2)

        self.loggerr.info("************ Entering Right name  **************")
        self.ff.typeRightName(self.R_name)
        time.sleep(2)

        self.loggerr.info("************ Entering Right message  **************")
        self.ff.typeRightMessage(self.R_message)
        time.sleep(3)

        self.loggerr.info("************ Calculating captcha  **************")
        Two_numbers = self.driver.find_element(By.CLASS_NAME, 'et_pb_contact_captcha_question').text
        Two = re.findall('\d+', Two_numbers)
        res = [int(x) for x in Two]
        total = 0
        for i in range(0, len(res)):
            total = total + res[i]

        self.loggerr.info("************ Inserting answer **************")
        R_Pass_the_answer = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[1]/div/div/div/article/div/div[1]/div/div/div[2]/div[2]/div/div[2]/form/div/div/p/input')
        R_Pass_the_answer.send_keys(total)
        time.sleep(3)

        self.loggerr.info("************ Right Submit click  **************")
        self.ff.R_submit_click()

        self.loggerr.info("************ Closing browser **************")
        self.driver.close()

        self.loggerr.info("************ Test 004 - End  **************")


