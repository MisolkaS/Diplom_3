
from selenium.webdriver.common.by import By

class IndexPageLocators:
    LENTA_ZAKAZOV_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Лента Заказов')]")
    MODAL_WINDOW_INGREDIENTS = (By.CLASS_NAME, "Modal_modal_overlay__x2ZCr")
    KONSTRUKTOR_BUTTON = (By.XPATH,   "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Конструктор')]")
    ALL_INGREDIENTS = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")
    MODAL_WINDOW_HEADER_LOCATOR = (By.XPATH, "//h2[contains(text(), 'Детали ингредиента')]")
    MODAL_WINDOW_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__TnseK')]")
    MODAL_WINDOW = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened__3ISw4')]")
    MODAL_WINDOW_ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq')]")
    MODAL_WINDOW_LOADING_LAYER = (By.CLASS_NAME, "Modal_modal__loading__3534A")
    FIRST_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient__1TVf6')]")
    PERSONAL_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    PERSONAL_ACCOUNT_AUTH = (By.XPATH, '//a[@class="AppHeader_header__link__3D_hX" and contains(., "Личный Кабинет")]')
    BASKET_INGREDIENT = (By.XPATH, '//p[text()="Соус Spicy-X" and contains(@class, "BurgerIngredient_ingredient__text__yp3dH")]')
    BASKET_INGREDIENT_1 = (By.XPATH, '//p[text()="Краторная булка N-200i" and contains(@class, "BurgerIngredient_ingredient__text__yp3dH")]')
    BASKET_INGREDIENT_2 = (By.XPATH, '//p[text()="Соус традиционный галактический" and contains(@class, "BurgerIngredient_ingredient__text__yp3dH")]')
    BASKET_INGREDIENT_3 = (By.XPATH, '//p[text()="Биокотлета из марсианской Магнолии" and contains(@class, "BurgerIngredient_ingredient__text__yp3dH")]')

    BASKET = (By.XPATH, '//ul[contains(@class, "BurgerConstructor_basket")]')
    COUNTER = (By.XPATH, '//p[text()="Соус Spicy-X"]/ancestor::a//p[@class="counter_counter__num__3nue1"]')
    ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")

class FeedPageLocators:
    ORDERS_LIST = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r') and contains(@class, 'mb-6')]")
    ORDER_LINK = (By.CLASS_NAME, "OrderHistory_link__1iNby")
    ORDER_TITLE = (By.TAG_NAME, "h2")
    LENTA_ZAKAZOV_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Лента Заказов')]")
    ORDER_ITEMS = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")
    ORDER_NUMBER = (By.CLASS_NAME, "text_type_digits-default")
    KONSTRUKTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Конструктор')]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    TOTAL_ORDERS_COUNTER_FOR_DAY = (By.XPATH,
                            "//p[contains(text(), 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'OrderFeed_number__2MbrQ')]")

    ORDERS_IN_PROGRESS = (By.CSS_SELECTOR, ".OrderFeed_orderListReady__1YFem .text")
    ORDER_NAME = (By.XPATH, "//h2[contains(@class, 'text text_type_main-medium mb-2')]")
class PersonalAccountPageLocators:
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
    PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")
    LOGIN_BUTTON = (By.XPATH, '//button[contains(@class, "button_button__33qZ0")]')
    HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")
    PASSWORD_RECOVERY = (By.XPATH, "//a[text()='Восстановить пароль']")
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    EYE_ICON = (By.CSS_SELECTOR, ".input__icon svg")
    MY_ORDERS = (By.XPATH,
     "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, 'text_type_digits-default')]")

class ForgotPasswordPageLocators:
    RECOVERY_BUTTON = (By.XPATH, "//button[contains(text(), 'Восстановить')]")
    EMAIL_FIELD = (By.XPATH, '//input[@name="name"]')
