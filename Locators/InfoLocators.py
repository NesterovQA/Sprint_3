from selenium.webdriver.common.by import By


class TestLocatorsInfoLocators:
    # InfoLocators:
    FALSE_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")
    ASSEMBLE_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")
