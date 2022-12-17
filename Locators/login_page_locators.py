from selenium.webdriver.common.by import By


class LoginPageLocators:
    # LoginPageLocators:
    FIELD_NAME = (By.XPATH, '(//*[contains(@class, "text input__textfield")])[1]')
    FIELD_EMAIL = (By.XPATH, '(//*[contains(@class, "text input__textfield")])[2]')
    #                          //*[contains(@class, "text input__textfield")]
    FIELD_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    BUTTON_ENTER = (By.XPATH, ".//*[text()='Войти']")
    BUTTON_ENTER_IF_ALREADY_REGISTR = (By.XPATH, ".//a[@href='/login']")
    BUTTON_RECOVERY_PASS = (By.XPATH, ".//a[@href='/forgot-password']")
