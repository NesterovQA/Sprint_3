from selenium.webdriver.common.by import By


class MainPageLocators:
    # MainPageLocators:
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(),'Войти в аккаунт')]")
    CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")
    ORDER_FEED = (By.XPATH, ".//p[text()='Лента Заказов']")
    LOGO = (By.XPATH, ".//a[@href='/']")

    BUTTON_ROLLS = (By.XPATH, ".//div/div/*[text()='Булки']")
    BUTTON_SAUCES = (By.XPATH, ".//div/div/*[text()='Соусы']")
    BUTTON_FILLINGS = (By.XPATH, ".//div/div/*[text()='Начинки']")
    TEXT_ROLLS = (By.XPATH, ".//h2[text()='Булки']")
    TEXT_SAUCES = (By.XPATH, ".//h2[text()='Соусы']")
    TEXT_TOPPINGS = (By.XPATH, ".//h2[text()='Начинки']")
    FILLINGS_LOCATOR = (By.XPATH, ".//img[@alt='Филе Люминесцентного тетраодонтимформа']")
    SAUCES_LOCATOR = (By.XPATH, ".//img[@alt='Соус с шипами Антарианского плоскоходца']")
    ROLLS_LOCATOR = (By.XPATH, ".//img[@alt='Флюоресцентная булка R2-D3']")
