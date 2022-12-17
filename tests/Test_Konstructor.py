import time
from locators.login_page_locators import LoginPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestKonstructor:

    def test_transfer_to_rolls_on_main_page(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку войти в аккаунт и нажал
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # ввожу данные в поля для входа и вхожу в аккаунт
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()

        # жду и ищу кнопку ночинки и жму на нее
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.BUTTON_FILLINGS))
        driver.find_element(*MainPageLocators.BUTTON_FILLINGS).click()
        time.sleep(1)
        # жду пока прокрутится до начинок и нажимаю на булки
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.FILLINGS_LOCATOR))
        driver.find_element(*MainPageLocators.BUTTON_ROLLS).click()
        assert driver.find_element(*MainPageLocators.ROLLS_LOCATOR).is_displayed()

    def test_transfer_to_sauces_on_main_page(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку войти в аккаунт и нажал
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # ввожу данные в поля для входа и вхожу в аккаунт
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()
        # жду и ищу кнопку соусы и жму на нее
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.BUTTON_SAUCES))
        driver.find_element(*MainPageLocators.BUTTON_SAUCES).click()
        # жду пока соусы появится в поле зрения и проверяю что она видима
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.SAUCES_LOCATOR))
        assert driver.find_element(*MainPageLocators.FILLINGS_LOCATOR).is_displayed()

    def test_transfer_to_fillings_on_mine_page(self, driver):
        # Регистрация
        user_mail = 'Vitalii_Nesterov_05_622@yandex.ru'
        user_password = '123456'
        driver.get("https://stellarburgers.nomoreparties.site/")
        # нашел кнопку войти в аккаунт и нажал
        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        # ожидаю загрузку элемента
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".button_button__33qZ0")))
        # ввожу данные в поля для входа и вхожу в аккаунт
        driver.find_element(*LoginPageLocators.FIELD_NAME).send_keys(user_mail)
        driver.find_element(*LoginPageLocators.FIELD_PASSWORD).send_keys(user_password)
        driver.find_element(*LoginPageLocators.BUTTON_ENTER).click()
        # жду и ищу кнопку ночинки и жму на нее
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(MainPageLocators.BUTTON_FILLINGS))
        driver.find_element(*MainPageLocators.BUTTON_FILLINGS).click()
        # жду пока начинка появится в поле зрения и проверяю что она видима
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.FILLINGS_LOCATOR))
        assert driver.find_element(*MainPageLocators.FILLINGS_LOCATOR).is_displayed()
