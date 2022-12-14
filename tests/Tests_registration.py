from Locators.infoLocators import TestLocatorsInfoLocators
from Locators.loginPageLocators import TestLocatorsLoginPageLocators
from Locators.mainpagelocators import TestLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Locators.registrationPageLocators import TestLocatorsRegistrationPageLocators


# Регистрация
class TestRegistration:
    def test_registration_base(self):
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # нашел кнопку зарегистрироваться около"вы новый нользователь?"
        driver.find_element(*TestLocatorsRegistrationPageLocators.BUTTON_REGISTRATION_NEW).click()
        # ввожу данные в поля регистрации
        driver.find_element(*TestLocatorsLoginPageLocators.FIELD_NAME).send_keys("Vitalii")
        driver.find_element(*TestLocatorsLoginPageLocators.FIELD_EMAIL).send_keys(user_mail)
        driver.find_element(*TestLocatorsLoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*TestLocatorsRegistrationPageLocators.BUTTON_REGISTRATION).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"
        driver.quit()

    def test_registration_password_lower_6_show_error(self):
        # регистрация и появление ошибки с неккоректным паролем
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        uncorrect_password = '12345'
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # нашел кнопку зарегистрироваться около "вы новый нользователь?"
        driver.find_element(*TestLocatorsRegistrationPageLocators.BUTTON_REGISTRATION_NEW).click()
        # ввожу данные в поля регистрации
        driver.find_element(*TestLocatorsLoginPageLocators.FIELD_NAME).send_keys("Vitalii")
        driver.find_element(*TestLocatorsLoginPageLocators.FIELD_EMAIL).send_keys(user_mail)
        driver.find_element(*TestLocatorsLoginPageLocators.FIELD_PASSWORD).send_keys(uncorrect_password)
        driver.find_element(*TestLocatorsRegistrationPageLocators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*TestLocatorsInfoLocators.FALSE_PASSWORD).is_displayed()
        driver.quit()