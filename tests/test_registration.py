from locators.info_locators import InfoLocators
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.registration_page_locators import RegistrationPageLocators


# Регистрация
class TestRegistration:
    def test_registration_base(self, driver):
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # нашел кнопку зарегистрироваться около"вы новый нользователь?"
        driver.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION_NEW).click()
        # ввожу данные в поля регистрации
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys("Vitalii")
        driver.find_element(*LoginPageLocators.FIELD_EMAIL).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION).click()
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/register"

    def test_registration_password_lower_6_show_error(self, driver):
        # регистрация и появление ошибки с неккоректным паролем
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        uncorrect_password = '12345'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # нашел кнопку зарегистрироваться около "вы новый нользователь?"
        driver.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION_NEW).click()
        # ввожу данные в поля регистрации
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys("Vitalii")
        driver.find_element(*LoginPageLocators.FIELD_EMAIL).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(uncorrect_password)
        driver.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION).click()
        assert driver.find_element(*InfoLocators.FALSE_PASSWORD).is_displayed()
