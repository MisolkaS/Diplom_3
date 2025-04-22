import allure
from locators import ForgotPasswordPageLocators
from pages.base_page import BasePage

class ForgotPasswordPage(BasePage):
    def __init__(self, driver, forgot_password_url):
        super().__init__(driver)
        self.forgot_password_url = forgot_password_url
        self.locators = ForgotPasswordPageLocators()

    @allure.title('Заполняем поле email')
    def p_email_recovery(self, email):
        self.f_wait_and_send_keys(self.locators.EMAIL_FIELD, email)

    @allure.title('Кликаем на кнопку Восстановить')
    def p_click_button_recovery(self):
        self.f_click_element(self.locators.RECOVERY_BUTTON)

    @allure.step('Ждем загрузки страницы')
    def p_wait_page(self, reset_password_url):
        self.f_wait_page(reset_password_url)