from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Login:
    textbox_email_id = 'user[email]'
    textbox_password_id = 'user[password]'
    button_signin_xpath = '//*[@id="sign_in_a65a8662b2"]/div[4]/input'
    click_by_xpath_atomation = '//*[@id="post-507"]/div/div[1]/div/div[2]/div/div[1]/div/div/div/div/ul/li[6]/a'
    link_logout_linktext = 'Sign Out'



    def __init__(self, driver):
        self.driver = driver

    def goToLogin(self):
        click_login = self.driver.find_element(By.LINK_TEXT, 'Login automation')
        click_login.click()

    def setUserEmail(self,useremail):
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(useremail)

    def setUserPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickSignIn(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign in').click()


    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext)
