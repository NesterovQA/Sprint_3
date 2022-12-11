import time
from locators import TestLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# регистрация и появление ошибки с неккоректным паролем
user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
uncorrect_password = '12345'
driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")
# нашел кнопку личный кабинет/нажал на нее
driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
# ожидаю загрузку элемента
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
# нашел кнопку зарегистрироваться около"вы новый нользователь?"
driver.find_element(*TestLocators.BUTTON_REGISTRATION_NEW).click()
# ввожу данные в поля регистрации
driver.find_element(*TestLocators.FIELD_NAME).send_keys("Vitalii")
driver.find_element(*TestLocators.FIELD_EMAIL).send_keys(user_mail)
driver.find_element(*TestLocators.FIELD_PASSWORD).send_keys(uncorrect_password)
driver.find_element(*TestLocators.BUTTON_REGISTRATION).click()
assert driver.find_element(*TestLocators.FALSE_PASSWORD).is_displayed()
driver.quit()


