
from selenium import webdriver
from selenium.webdriver.common.by import By



class HTML_table:

    # autom_execise_by_XPATH = "//*[@id='menu-home-page-menu']/li[5]/a"
    # inter_simple_el_by_XPATH = "//a[normalize-space()='Interactions with simple elements']"
    table_with_id_by_XPATH ="//table[contains(@id,'htmlTableId')]/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def goToAutomate(self):
        auto_click = self.driver.find_element(By.XPATH,"//*[@id='menu-home-page-menu']/li[5]/a")
        auto_click.click()


    def goTo_Elemenets(self):
        ele_click = self.driver.find_element(By.XPATH,"//a[normalize-space()='Interactions with simple elements']")
        ele_click.click()


    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0,600)")

    def close_driver(self):
        self.driver.close()