from time import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

'''
Webelement class: handling js Alert , ok, cancel, entering text, switch_to.Alert practice here: https://courses.letskodeit.com/practice
'''
#VARIABLES
HOST = "https://courses.letskodeit.com/practice"
filepath = '../screenshots/'
name_input_xpath = "//input[@name='enter-name']"
name = 'John Doe'

# STEPS
# 1. open the browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
driver.maximize_window()


def tes_alert_single_button():
    # 2. open the website
    print('opening the page...')
    driver.get(HOST)
    # enter name
    print("testing the alert button...")
    name_input = driver.find_element(By.XPATH, name_input_xpath)
    name_input.send_keys(name)
    # click on alert
    driver.find_element(By.ID, "alertbtn").click()
    # switch to alert
    alert = driver.switch_to.alert
    # get the text
    print('Alert text: ', alert.text)
    # click OK on alert
    sleep(5)
    alert.accept()  # clicking the ok button
    print("############ accepted the alert #############")
    sleep(5)


def tes_alert_multi_button():
    # 2. open the website
    print('opening the page...')
    driver.get(HOST)
    print("testing the confirm button ...")
    # enter name
    name_input = driver.find_element(By.XPATH, name_input_xpath)
    name_input.send_keys(name)
    # click on Confirm
    driver.find_element(By.ID, 'confirmbtn').click()
    # switch to alert, create Alert object that shows you available methods
    alert2 = driver.switch_to.alert
    # get the text
    print('Alert text: ', alert2.text)
    sleep(5)
    alert2.dismiss() # clicking the cancel button
    print("############ canceled the alert #############")
