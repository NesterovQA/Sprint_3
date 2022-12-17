from selenium.webdriver.common.by import By


class ProfileLocators:
    # ProfileLocators:
    # BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")
    BUTTON_EXIT = (By.XPATH, '//*[contains(@class, "Account_button")]')
    BUTTON_ORDER = (By.XPATH, ".//button(text(),'Оформить заказ')]")
    BUTTON_ACCOUNT_PROFILE = (By.XPATH, ".//a[@href='/account/profile']")
