from time import *

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# VARIABLES - Test Data

filepath = '../screenshots/'



def click_element_by_locator(driver, locator, method='xpath', wait_time=10):
    """click with explicit wait"""
    try:
        wdwait = WebDriverWait(driver, wait_time)
        # elem = driver.find_element(xpath) - this is with implicit wait
        element = object  # very general data type
        if method == 'xpath':
            element = wdwait.until(EC.presence_of_element_located((By.XPATH, locator)))
        elif method == 'id':
            element = wdwait.until(EC.presence_of_element_located((By.ID, locator)))
        elif method == 'css':
            element = wdwait.until(EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        element.click()
    except (NoSuchElementException, TimeoutException) as err:
        print("Error on click element by locator, check locator", locator)
        print(err)


def test_go_to_authentication_page(driver):
    # 2. open the http://automationpractice.com/index.php demo website
    driver.get("http://automationpractice.com/index.php")
    # click on sign in
    sign_in_link = "//a[contains(text(), 'Sign in')]"
    # option 1, to click using regular find_element method
    driver.find_element(By.XPATH, sign_in_link).click()
    # option 2, to use function we created above with explicit wait
    click_element_by_locator(sign_in_link)
    # click_element_by_xpath(sign_in_link, 20)
    sleep(3)


def test_create_account(driver, email):
    """
        Creating the account with email and static data for the sign up info
        This step is dependent on test_go_to_authentication_page()
        :param email: email with @ symbol and dot to be included
    """
    # Variable
    cust_fname = 'John'
    cust_lname = 'Doe'
    password = 'ForgetMeAsUsual123'
    state = 'New Jersey'

    # enter email address to Create an Account field, mycool@email.com, click on create account
    driver.find_element(By.ID, "email_create").send_keys(email)
    driver.find_element(By.ID, "SubmitCreate").click()
    sleep(3)

    # radio button: click on Mr
    mr_gender = driver.find_element(By.ID, "id_gender1")
    mrs_gender = driver.find_element(By.ID, "id_gender2")
    mrs_gender.click()
    click_element_by_locator('id_gender2', method='id')

    # Enter first name
    cfirst_name = driver.find_element(By.NAME, "customer_firstname")
    cfirst_name.send_keys(cust_fname)

    # Enter last name
    clast_name = driver.find_element(By.NAME, "customer_lastname")
    clast_name.send_keys(cust_lname)

    # Enter Password
    driver.find_element(By.ID, "passwd")

    # Check Sign up for our newsletter
    nl_checkbox = driver.find_element(By.ID, "newsletter")
    nl_checkbox.click()
    sleep(5)
    driver.save_screenshot(filepath + 'signup1.png')

    # clear it and enter different name
    cfirst_name.clear()
    cfirst_name.send_keys('Jonathan')

    # verify email, get text, make sure it is what we entered
    # verify Mr is selected
    print("Is gender type MR selected? - ", mr_gender.is_selected())
    print("Is gender type MRS selected? - ", mrs_gender.is_selected())
    if mrs_gender.is_selected():
        mr_gender.click()

    print("Is gender type MR selected? - ", mr_gender.is_selected())
    print("Is gender type MRS selected? - ", mrs_gender.is_selected())

    # verify Sign up is checked
    print("Is Sign Up checkbox is checked? - ", nl_checkbox.is_selected())

    # verify One of the Error messages when required field is not entered
    address_msg_xpath = "//input[@id='address1']/../span"
    address_msg_elem = driver.find_element(By.XPATH, address_msg_xpath)
    address_msg = ""
    if address_msg_elem.is_displayed():
        address_msg = driver.find_element(By.XPATH, address_msg_xpath).text
    else:
        print("Address message is not displayed.")
    print("address_msg displayed: ", address_msg)
    driver.save_screenshot(filepath + 'signup2.png')

# Drop down Select State
    # verify state is selected
    # html DOM - document object model
    # driver.execute_script('arguments[0].click();', driver.find_element(By.ID, 'someid')
    driver.execute_script('window.scrollBy(0,800)')  # executing java script code

    state_ddown = Select(driver.find_element(By.ID, 'id_state'))

    state_ddown.select_by_value('2')
    # state_ddown.options - returns all available options
    print('current selections: ', state_ddown.all_selected_options[0].text)  # returns all selected options
    sleep(5)
    state_ddown.select_by_visible_text('California')
    print('current selections: ', state_ddown.all_selected_options[0].text)  # returns all selected options
    sleep(5)
    state_ddown.select_by_index(2)
    print('current selections: ', state_ddown.all_selected_options[0].text)  # returns all selected options

    # H/W
    # ...
    # click on Register


def test_explicit_wait(driver):
    # open the website
    host = "https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver"
    driver.get(host)
    print("########### Testing Populate text #############")
    click_element_by_locator('populate-text', 'id')
    wdwait = WebDriverWait(driver, 15)
    wdwait.until(EC.text_to_be_present_in_element((By.ID, 'h2'), 'Selenium'))
    element = wdwait.until(EC.presence_of_element_located((By.ID, 'h2')))
    print("Text in the element", element.text)

    print("########## Testing Visibility of element #############")
    click_element_by_locator("display-other-button")
    button_text = wdwait.until(EC.visibility_of_element_located((By.ID, 'hidden'))).text
    print("Text inside the button", button_text)


def test_drag_drop(driver):
    print("######### Testing Drag and drop ")
    driver.get("https://jqueryui.com/droppable/")
    wdwait = WebDriverWait(driver, 20)
    driver.switch_to.frame(0)
    source_element = wdwait.until(EC.presence_of_element_located((By.ID, 'draggable')))
    target_element = wdwait.until(EC.presence_of_element_located((By.ID, 'droppable')))
    print(f"Original text in the box: '{target_element.text}'")
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()
    print(f"text in the box after drag and drop: '{target_element.text}'")


def test_mouse_hover_over(driver):
    wdwait = WebDriverWait(driver, 20)

    driver.get("http://automationpractice.com/index.php")
    driver.execute_script('window.scrollBy(0,800)')  # executing java script code

    product1 = wdwait.until(EC.presence_of_element_located((By.XPATH, "//ul[@id='homefeatured']/li[1]")))
    actions = ActionChains(driver)
    actions.move_to_element(product1).perform()
    driver.find_element(By.LINK_TEXT, 'Add to cart').click()