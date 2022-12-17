from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.profile_locators import ProfileLocators


class TestPersonalAccount:

    def test_transfer_to_personal_account(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # ввожу данные в поля для входа в аккаунт
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        # перехожу в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(ProfileLocators.BUTTON_ACCOUNT_PROFILE))
        assert driver.find_element(*ProfileLocators.BUTTON_ACCOUNT_PROFILE).is_displayed()

    def test_transfer_to_konstructor_from_personal_account_on_click_konstructor(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # ввожу данные в поля для входа в аккаунт
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        # перехожу в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # перехожу в конструктор по кнопке конструктор
        driver.find_element(*MainPageLocators.CONSTRUCTOR).click()
        cur_url = 'https://stellarburgers.nomoreparties.site/'
        assert driver.current_url == cur_url

    def test_transfer_to_konstructor_from_personal_account_on_click_logo(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # ввожу данные в поля для входа в аккаунт
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT))
        # перехожу в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # перехожу в конструктор по кнопке Logo
        driver.find_element(*MainPageLocators.LOGO).click()
        cur_url = 'https://stellarburgers.nomoreparties.site/'
        assert driver.current_url == cur_url

    def test_exit_from_account(self, driver):
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку личный кабинет/нажал на нее
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # ввожу данные в поля для входа в аккаунт
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(LoginPageLocators.BUTTON_ENTER))
        # перехожу в личный кабинет
        driver.find_element(*MainPageLocators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(ProfileLocators.BUTTON_EXIT))
        # выхожу из аккаунта
        driver.find_element(*ProfileLocators.BUTTON_EXIT).click()
        cur_url = 'https://stellarburgers.nomoreparties.site/account'
        assert cur_url in driver.current_url
