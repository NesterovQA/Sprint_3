from selenium.webdriver.common.by import By


class TestLocatorsRegistrationPageLocators:
    # RegistrationPageLocators(LoginPageLocators):
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    BUTTON_REGISTRATION_NEW = (By.XPATH, ".//a[@href='/register']")
