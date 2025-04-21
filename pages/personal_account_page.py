import allure
from locators import PersonalAccountPageLocators
from pages.base_page import BasePage

class PersonalAccountPage(BasePage):
    def __init__(self, driver, personal_account_url):
        super().__init__(driver)
        self.personal_account_url = personal_account_url
        self.locators = PersonalAccountPageLocators()

    @allure.title('Авторизация пользователя')
    def p_login_user(self, email, password):
        self.f_wait_and_send_keys(self.locators.EMAIL_FIELD, email)
        self.f_wait_and_send_keys(self.locators.PASSWORD_FIELD, password)
        self.f_click_element(self.locators.LOGIN_BUTTON)


    @allure.title('Заполняем пароль пользователя')
    def p_enter_password(self, password):
        self.f_wait_and_send_keys(self.locators.PASSWORD_FIELD, password)

    @allure.title('Кликаем на глаз в поле пароля')
    def p_click_eye(self):
        self.f_click_eye(self.locators.EYE_ICON)

    @allure.title('Получаем тип поля')
    def p_get_attribute_type(self):
        el_type = self.f_get_attribute_type(self.locators.PASSWORD_FIELD)
        return el_type

    @allure.title('Кликаем на кнопку История заказов')
    def p_click_orders_history(self):
        self.f_click_element(self.locators.HISTORY_BUTTON)

    @allure.title('Кликаем на кнопку Выход')
    def p_click_logout(self):
        self.f_click_element(self.locators.LOGOUT_BUTTON)

    @allure.title('Кликаем на ссылку Восстановить пароль')
    def p_click_password_recovery(self):
        self.f_click_element(self.locators.PASSWORD_RECOVERY)

    @allure.title('Заполняем поле email')
    def p_email_recovery(self, email):
        self.f_wait_and_send_keys(self.locators.EMAIL_FIELD, email)

    @allure.step('Ждем загрузки страницы')
    def p_wait_page(self, url):
        self.f_wait_page(url)
    @allure.title('Получаем список своих заказов')
    def p_count_user_orders(self):
        order_elements = self.f_wait_any_elements(self.locators.MY_ORDERS)
        order_numbers = [element.text for element in order_elements]
        return order_numbers








