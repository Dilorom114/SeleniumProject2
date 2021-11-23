from src.webelement_alerts import *
from webelement_class import *

email = 'mycool@email.com'

# STEPS
# 1. open the browser
driver = webdriver.Chrome()
driver.implicitly_wait(20)  # synchronizing the browser
driver.maximize_window()

# tes_alert_single_button()
# tes_alert_multi_button()

# tes_go_to_authentication_page()
# tes_create_account(email)
# tes_explicit_wait()
# tes_drag_drop()

tes_mouse_hover_over(driver)

sleep(5)
driver.quit()