#  Section 1 :
# information was taken via Ubuntu where I run the command
# :curl https://ultimate.com -Iv | grep 'Server certificate' and stored it in txt file
# this method test_SSl_cert goes to Documentation to that txt file and loking for start, expire dates in that file
# and printing them out with current date

import datetime

import pytest
from colorama import Fore
import allure
from utilities.customLogger import LogGen

loggerr = LogGen.loggen()

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
def test_SSL_cert():
    loggerr = LogGen.loggen()
    loggerr.info("************ Test 003 - Start  **************")
    file = open('../Documents/Info_from_Ubuntu_SSL.txt', 'r')
    loggerr.info("************ Reading from the txt file  **************")
    read = file.readlines()
    for Start_date in read:
        if Start_date.startswith('  start date:'):
            loggerr.info("************ Extract start date  **************")
            print(Fore.GREEN + f"\n SSl Cerificate information about start date:\n  ",  Start_date.strip())

    for EXP_date in read:
        if EXP_date.startswith('  expire date:'):
            loggerr.info("************ Extract Expire date  **************")
            print(Fore.RED + f" SSl Cerificate information about expiration date:\n  ",  EXP_date.strip())
    loggerr.info("************  Current date  **************")
    currentdate = datetime.datetime.now()
    print(Fore.BLUE + f" Today is :\n " , currentdate)
    loggerr.info("************ Test 003 - End  **************")

test_SSL_cert()
