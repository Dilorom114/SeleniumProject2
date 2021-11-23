# from src.webelement_alerts import *
# from src.webelement_class import *

import pytest

@pytest.mark.myfirstCase
@pytest.mark.sample1
@pytest.mark.regression
def test_sample_pytst(driver):
    assert 25/5 == 5
    print("\n test 1 yeah this is the first pytest executions")
# email = 'mycool@email.com'
# # STEPS
# # 1. open the browser
# driver = webdriver.Chrome()
# driver.implicitly_wait(20)  # synchronizing the browser
# driver.maximize_window()
#
# # test_alert_single_button()
# # test_alert_multi_button()
#
# # test_go_to_authentication_page()
# # test_create_account(email)
# # test_explicit_wait()
# # test_drag_drop()
# test_mouse_hover_over(driver)
#
# assert sum_of_num(3, 4) == 7
# assert sum_of_num(-1, 6) == 5
# assert divide_num(4, 2) == 2
# assert divide_num(3, 0) !=0
# sleep(5)
# driver.quit()

@pytest.mark.mySecondCase
@pytest.mark.regression
def test_sample_pytst2():
    print("test2")
    assert 25 / 5 == 65

