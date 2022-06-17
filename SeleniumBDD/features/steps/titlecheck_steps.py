from behave import *                       # ( given , when , then )
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given('launch browser')
def launchBrowser(context):
    # context.driver = webdriver.Chrome(executable_path="C:\serge\OneDrive\Desktop\drivers\chromedriver.exe")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    time.sleep(2)


@when('open ultimateqa.com homepage')
def openHomePage(context):
    context.driver.get("https://ultimateqa.com/")
    time.sleep(2)

@then('verify that title is "Home | Ultimate QA"')
def verifyTitle(context):
    actual_Title = context.driver.title
    if actual_Title == "Home | Ultimate QA":
        assert True
    else:
        print(f"Title is not mathcing : ", actual_Title)
        assert False

time.sleep(2)
@then('close browser')
def closeBrowser(context):
    context.driver.close()

