from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.registration_page_locators import RegistrationPageLocators


class TestLogin:

    def test_login_button_on_mane_page(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку войти в аккаунт и нажал
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # ввожу данные в поля для входа
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()
        assert driver.find_element(*MainPageLocators.LOGO).is_displayed()

    def test_login_button_in_personal_account(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # ввожу данные в поля для входа
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()
        assert driver.find_element(*MainPageLocators.LOGO).is_displayed()

    def test_login_button_in_registration_form(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # нашел кнопку зарегистрироваться около"вы новый нользователь?"
        driver.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION_NEW).click()
        # нашел кнопку "войти" около уже зарегистрированы?
        driver.find_element(*LoginPageLocators.BUTTON_ENTER_IF_ALREADY_REGISTR).click()
        # ввожу данные для входа
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

    def test_login_button_in_recovery_password_form(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # нажимаю восстановить пароль
        driver.find_element(*LoginPageLocators.BUTTON_RECOVERY_PASS).click()
        # нажимаю войти
        driver.find_element(*LoginPageLocators.BUTTON_ENTER_IF_ALREADY_REGISTR).click()
        # ввожу данные в поля для входа
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()
        assert driver.find_element(*MainPageLocators.LOGO).is_displayed()
