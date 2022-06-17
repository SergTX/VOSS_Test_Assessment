from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@when('open home page')
def open_HomePage(context):
    context.driver.get("https://ultimateqa.com/")
    time.sleep(2)

@when('navigate to atutomation execises')
def goToAutomationExercises(context):
    aut_exer = context.driver.find_element(By.LINK_TEXT, 'Automation Exercises')
    aut_exer.click()
    time.sleep(2)

@when('click on "Login automation"')
def click_login(context):
    login = context.driver.find_element(By.LINK_TEXT, 'Login automation')
    login.click()
    time.sleep(2)

@when('validate the title of the page')
def titleValidate(context):
    actual_title = context.driver.title
    if actual_title == "Ultimate QA":
        print(f"Title is : ", actual_title)
        assert True
    else:
        print(f"Title is not mathcing : ", actual_title)
        assert False

@when('Enter username "{email}" and password "{password}"')
def login(context, email,password):
    context.driver.find_element(By.ID, 'user[email]').send_keys(email)
    context.driver.find_element(By.ID, 'user[password]').send_keys(password)
    time.sleep(2)

@then('User must be successfully login to the website')
def click_SignIn(context):
    context.driver.find_element(By.XPATH, '//*[@id="sign_in_a65a8662b2"]/div[4]/input').click()

