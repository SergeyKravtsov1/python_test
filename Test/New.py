from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Настройка опций для браузера (например, отключение режима headless)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Если хотите запустить в headless-режиме
# Инициализация веб-драйвера
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# Переход на нужный сайт
driver.get("https://sportsbook.paridirect.com/velisportsbook/dev")
# Ожидание появления и клик на кнопку входа

# Ожидание появления поля ввода кода и клик на него
code_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@name='code']"))
)
code_input.click()
# Завершение работы с веб-драйвером
# driver.quit()  # Закрытие браузера (закомментируйте, если хотите продолжать работу)