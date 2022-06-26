import pytest
from selenium.webdriver.common.by import By


class Fill_forms:

    left_name_by_id = 'et_pb_contact_name_0'
    left_message_by_xpath = '//*[@id="et_pb_contact_message_0"]'
    left_submit_by_name = 'et_builder_submit_button'
    right_name_bi_id = 'et_pb_contact_name_1'
    right_message_by_xpath = '//*[@id="et_pb_contact_message_1"]'
    right_submit_by_xpath = '//*[@id="et_pb_contact_form_1"]/div[2]/form/div/button'

    def __init__(self, driver):
        self.driver = driver

    def typeLeftName(self,L_name):
        self.driver.find_element(By.ID,self.left_name_by_id).send_keys(L_name)

    def typeLeftMessage(self,L_message):
        self.driver.find_element(By.XPATH,self.left_message_by_xpath).send_keys(L_message)

    def L_submit_click(self):
        self.driver.find_element(By.NAME, self.left_submit_by_name).click()

    def typeRightName(self,R_name):
        self.driver.find_element(By.NAME, self.right_name_bi_id).send_keys(R_name)

    def typeRightMessage(self,R_message):
        self.driver.find_element(By.XPATH,self.right_message_by_xpath).send_keys(R_message)

    def R_submit_click(self):
        self.driver.find_element(By.XPATH, self.right_submit_by_xpath).click()
