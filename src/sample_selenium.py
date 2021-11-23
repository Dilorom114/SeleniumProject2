from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.thelevelupsolutions.com/")
driver.maximize_window()
driver.quit()  # close all tabs