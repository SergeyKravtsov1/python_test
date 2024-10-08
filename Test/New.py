from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://magento.softwaretestingboard.com/women/tops-women/tees-women.html")
sleep(2)
girl = driver.find_element(By.XPATH, "//ol[@class='products list items product-items']/li[@class='item product product-item'][1]")
print(girl.text)
# print(girl.get_attribute("href"))
sorter = driver.find_element(By.ID,'sorter')
select = Select(sorter)
select.select_by_value('price')
sleep(2)
girl = driver.find_element(By.XPATH, "//ol[@class='products list items product-items']/li[@class='item product product-item'][1]")
print(girl.text)
# print(girl.get_attribute("href"))