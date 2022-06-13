# Steps from # 1 - 5
#   unfortunately I don't have a knowledge about how to deal with captcha.
#
import logging

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_Auto_Page:
    urlmain_auto = ReadConfig.getURL()
    url_signin = ReadConfig.sign_URL()
    userEmail = ReadConfig.userEmail()
    userPassword = ReadConfig.userPW()


    loggerr = LogGen.loggen()


    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_AutoVerifyTitle(self,setup):
        self.loggerr.info("************ Test 001 - Start  **************")
        self.loggerr.info("******************Test Auto Verifcation of the Page ************* ")
        self.loggerr.info("************ Open browser **************")
        self.driver = setup
        self.driver.get(self.urlmain_auto)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        actual_title = self.driver.title
        if actual_title == 'Automation Practice | Ultimate QA':
            self.driver.save_screenshot("..//Screenshots//" + "test_AutoVerifyTitlePassed.png")
            self.driver.close()
            self.loggerr.info("************** VERIFIED  001 ********")
            self.loggerr.info("************ Closing browser **************")
            self.loggerr.info("************ Test 001 - End  **************")
            assert True
            print('\nTitle verified')
        else:
            self.loggerr.info("************ Title does not match  **************")
            print('\nTitle does not match. Please take a look.')
            self.driver.save_screenshot("..//Screenshots//" + "test_AutoVerifyTitleFailed.png")
            self.loggerr.info("************ Closing browser **************")
            self.loggerr.info("************ Test 001 - End  **************")
            self.driver.close()
            assert False

    time.sleep(3)


    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.severity(allure.severity_level.CRITICAL)
    def test_click_autologin(self,setup):
        self.loggerr.info("************ Test 002 - Start  **************")
        self.driver = setup
        self.driver.get(self.urlmain_auto)
        self.driver.maximize_window()
        self.loggerr.info("************ Going to Login Automation page  **************")
        click_login = self.driver.find_element(By.LINK_TEXT, 'Login automation')
        click_login.click()
        self.loggerr.info("************ Verifying Page Title 002 **************")
        actual_title = self.driver.title
        if actual_title == "Ultimate QA":
            self.driver.save_screenshot("..//Screenshots//" + "test_click_autologinPASSED.png")
            self.loggerr.info("************** VERIFIED  002 ********")
            assert True
        else:
            self.driver.save_screenshot("..//Screenshots//" + "test_click_autologinFAILED.png")
            self.loggerr.info("************ Title does not match  002 **************")
            assert False
        self.loggerr.info("************ Entering Email  **************")
        self.L=Login(self.driver)
        self.L.setUserEmail(self.userEmail)
        self.loggerr.info("************ Entering PassWord  **************")
        self.L.setUserPassword(self.userPassword)
        time.sleep(5)
        self.loggerr.info("************ Click on Sign In Button with Captcha  **************")
        self.driver.find_element(By.XPATH,'//*[@id="sign_in_0c85f3989c"]/div[4]/input').click()
        self.driver.save_screenshot("..//Screenshots//" + "SignIn.png")

        # after signed in = locating menu
        self.loggerr.info("************ Clicking on Menu  **************")
        menu_button = self.driver.find_element(By.XPATH, '/html/body/header/div/div/button/span[1]')
        menu_button.click()

        # clicking sign out
        self.loggerr.info("************ Click on Sign Out  **************")
        sign_out = self.driver.find_element(By.LINK_TEXT, ' Sign Out')
        sign_out.click()
        self.loggerr.info("************ Test 002 - End  **************")
        print("User signed out")




