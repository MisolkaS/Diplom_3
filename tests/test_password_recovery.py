import allure
from pages.personal_account_page import PersonalAccountPage
from pages.index_page import IndexPage
from pages.forgot_password_page import ForgotPasswordPage
from data.data_url import *
from data.data_user import *


class TestPasswordRecovery:
    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    def test_password_recovery_page_redirect(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)


        index_page.p_open_index_page()
        index_page.p_click_personal_account_page()
        personal_account_page.p_click_password_recovery()

        current_url = index_page.p_get_current_url()
        with allure.step('Проверка перехода на страницу восстановления пароля'):
            assert "/forgot-password" in current_url, f"Ожидался URL: {forgot_password_url}, но получен: {current_url}"
            allure.attach(f"Ожидаемый URL: {forgot_password_url}\nПолученный URL: {current_url}", name="URL details",
                          attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    def test_submit_recovery_form_with_email(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)
        forgot_password_page = ForgotPasswordPage(driver, forgot_password_url)

        index_page.p_open_index_page()
        index_page.p_click_personal_account_page()
        personal_account_page.p_click_password_recovery()

        forgot_password_page.p_email_recovery(registration_data['email'])
        forgot_password_page.p_click_button_recovery()
        forgot_password_page.p_wait_page(reset_password_url)

        current_url = index_page.p_get_current_url()
        with allure.step('Проверка перехода на форму восстановления пароля'):
            assert "/reset-password" in current_url, f"Ожидался URL: {reset_password_url}, но получен: {current_url}"

    @allure.title('Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его»')
    def test_click_recovery_password(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)

        index_page.p_open_index_page()
        index_page.p_click_personal_account_page()

        personal_account_page.p_enter_password(registration_data['password'])
        personal_account_page.p_click_eye()
        password_type = personal_account_page.p_get_attribute_type()
        with allure.step('Пароль видим после нажатия на иконку'):
            assert password_type == "text", "Пароль должен быть видимым после нажатия на иконку"

        personal_account_page.p_click_eye()
        password_type = personal_account_page.p_get_attribute_type()

        with allure.step('Пароль невидим после нажатия на иконку'):
            assert password_type == "password", "Пароль должен быть невидимым после нажатия на иконку"
