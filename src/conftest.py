import pytest
from time import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope='session')
def driver():
    # SETUP - steps to do before <scope>
    print("initializing")
    opts = Options()
    opts.add_argument("--disable-notifications")
    # 1. open the browser
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(20)  # synchronizing the browser
    driver.maximize_window()

    yield driver
    sleep(5)
    print("closing the browser")
    driver.quit()
    print("Test cases are completed!!!")


