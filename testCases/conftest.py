from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('\n Chrome browser is launched....\n')
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        print('\n Firefox browser is launched....\n')
    elif browser == "Medge":
        driver = webdriver.Edge()
        print('\n Microsoft Edge browser is launched....\n')
    return driver

def pytest_addoption(parser):   # will get the value from hooks
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):   # return Browser value to setup method
    return request.config.getoption('--browser')

