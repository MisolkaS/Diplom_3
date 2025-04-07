
from selenium.webdriver.common.by import By

class IndexPageLocators:
    LENTA_ZAKAZOV_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Лента Заказов')]")
    MODAL_WINDOW_INGREDIENTS = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    KONSTRUKTOR_BUTTON = (By.XPATH,   "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Конструктор')]")
    ALL_INGREDIENTS = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")
    MODAL_WINDOW_HEADER_LOCATOR = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    MODAL_WINDOW_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]")
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    PERSONAL_ACCOUNT_AUTH = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and contains(., "Личный Кабинет")]')
    BASKET_INGREDIENT = (By.XPATH, '//p[text()="Соус Spicy-X" and contains(@class, "BurgerIngredient_ingredient__text__yp3dH")]')
    BASKET = (By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket")]')
    COUNTER = (By.XPATH, '//p[text()="Соус Spicy-X"]/ancestor::a//p[@class="counter_counter__num__3nue1"]')
    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")

class FeedPageLocators:
    ORDERS_LIST = (
        By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r') and contains(@class, 'mb-6')]")
    ORDER_LINK = (By.CLASS_NAME, "OrderHistory_link__1iNby")
    ORDER_TITLE = (By.TAG_NAME, "h2")
    LENTA_ZAKAZOV_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Лента Заказов')]")




class PersonalAccountPageLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, '//button[contains(@class, "button_button__33qZ0")]')
    HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    PASSWORD_RECOVERY = (By.XPATH, "//a[text()='Восстановить пароль']")
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    EYE_ICON = (By.XPATH, "//div[@class='input__icon input__icon-action']")

# #главная страница
# xpath_enter_in_account_button = "//button[text()='Войти в аккаунт']" # Кнопка «Войти в аккаунт»
# xpath_of_order_button = "//section[2]//button"
# xpath_of_personal_page = ".//p[text()='Личный Кабинет']"
# xpath_of_menu = "//section[1]/div/div"
# xpath_of_h2 = "//h2"
#
# #страница логина
#
# xpath_email_login_input = "//fieldset[1]//input"  # Поле для ввода электронной почты
# xpath_password_login_input = "//fieldset[2]//input"  # Поле для ввода пароля
# xpath_login_button = "//button[text()='Войти']"
# xpath_constructor_button = "//p[text()='Конструктор']"
# xpath_logo_button = "//div/header/nav/div/a"  # логотип
# xpath_login_logout_button = "//button[text()='Выход']"
# xpath_password_error ="//div[contains(@class, 'input_type_password') and contains(@class, 'input_status_error')]"
#
#
# #страница регистрации
#
# xpath_name_input = "//fieldset[1]//input" # Поле для ввода имени
# xpath_email_input = "//fieldset[2]//input"  # Поле для ввода электронной почты
# xpath_password_input = "//fieldset[3]//input"  # Поле для ввода пароля
# xpath_link_enter = "//a[text()='Войти']"
# xpath_register_button = "//button[text()='Зарегистрироваться']"  # "//div//button" Кнопка для регистрации