from selenium.webdriver.common.by import By


class TestLocators:
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

    # LoginPageLocators:
    FIELD_NAME = (By.XPATH, '(//*[contains(@class, "text input__textfield")])[1]')
    FIELD_EMAIL = (By.XPATH, '(//*[contains(@class, "text input__textfield")])[2]')
    #                          //*[contains(@class, "text input__textfield")]
    FIELD_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    BUTTON_ENTER = (By.XPATH, ".//*[text()='Войти']")
    BUTTON_ENTER_IF_ALREADY_REGISTR = (By.XPATH, ".//a[@href='/login']")
    BUTTON_RECOVERY_PASS = (By.XPATH, ".//a[@href='/forgot-password']")
    # RegistrationPageLocators(LoginPageLocators):
    BUTTON_REGISTRATION = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    BUTTON_REGISTRATION_NEW = (By.XPATH, ".//a[@href='/register']")

    # ProfileLocators:
    # BUTTON_EXIT = (By.XPATH, ".//button[text()='Выход']")
    BUTTON_EXIT = (By.XPATH, '//*[contains(@class, "Account_button")]')
    BUTTON_ORDER = (By.XPATH, ".//button(text(),'Оформить заказ')]")
    BUTTON_ACCOUNT_PROFILE = (By.XPATH, ".//button[text()='Профиль']")
    # InfoLocators:
    FALSE_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")
    ASSEMBLE_BURGER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    # ListOfProducts:
    LIST_OF_ROLLS = (By.XPATH, ".//section/div/ul[1]/a")
    LIST_OF_SAUCES = (By.XPATH, ".//section/div/ul[2]/a")
    LIST_OF_TOPPINGS = (By.XPATH, ".//section/div/ul[3]/a")
