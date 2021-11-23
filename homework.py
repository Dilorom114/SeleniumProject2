import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://automationpractice.com/index.php")
driver.find_element(By.XPATH, "//a[@class = 'login']").click()
login = driver.find_element(By.XPATH, "//input[@id= 'email']")
login.send_keys('dilorom_a@yahoo.com')
passw = driver.find_element(By.XPATH, "//input[@id='passwd']")
passw.send_keys('M00v0zanat')
time.sleep(3)
driver.find_element(By.ID, "SubmitLogin").click()
# driver.find_element(By.XPATH, "//span[@xpath='1']").click()
# driver.find_element(By.XPATH, "//button[@type='submit']/span[@xpath='1']").click()
# driver.find_element(By.XPATH, "//button[@id='SubmitLogin']/span").click()
# driver.find_element(By.XPATH, "//button[@type='submit'] //i[@class='icon-lock left']").click()
print("Completed")
# driver.close()


# Drop