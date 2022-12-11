import time
from locators import TestLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Регистрация
user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
user_password = '123456'
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
# нашел кнопку личный кабинет/нажал на нее
driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
# ожидаю загрузку элемента
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))

# нажимаю восстановить пароль
driver.find_element(*TestLocators.BUTTON_RECOVERY_PASS).click()
# нажимаю войти
driver.find_element(*TestLocators.BUTTON_ENTER_IF_ALREADY_REGISTR).click()
# ввожу данные в поля для входа
driver.find_element(*TestLocators.FIELD_NAME).send_keys(user_mail)
driver.find_element(*TestLocators.FIELD_PASSWORD).send_keys(user_password)
driver.find_element(*TestLocators.BUTTON_ENTER).click()
assert driver.find_element(*TestLocators.LOGO).is_displayed()
driver.quit()