from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print('Chrome browser is launched....')
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        print('Firefox browser is launched....')
    return driver

def pytest_addoption(parser):   # will get the value from hooks
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):   # return Browser value to setup method
    return request.config.getoption('--browser')

