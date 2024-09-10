import time
from idlelib import browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sportsbook.paridirect.com/velisportsbook/dev")
login_button = driver.find_element(By.XPATH, '//button[@class="btn btn-small btn-white auth-btn"]').click()
time.sleep(2)
login_input = driver.find_element(By.XPATH, '//input[@type="tel"]').click()
login_input = driver.find_element(By.XPATH, '//input[@type="tel"]').send_keys("893804431")
password_input = driver.find_element(By.XPATH, '//input[@type="password"]').click()
password_input = driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("123456asdfaA@")
checkbox_button = driver.find_element(By.XPATH, '//span[@class="el-checkbox__inner"]').click()
element = driver.find_element(By.XPATH,'//button[@data-test-id="login__submit-cta"]')
driver.execute_script("arguments[0].scrollIntoView();", element)
driver.execute_script("arguments[0].click();", element)
driver.switch_to.frame(driver.find_element(By.ID, 'sportsbook-app'))
field_booking_code = driver.find_element(By.XPATH,"//input[@name='code']").click()
driver.quit()



