import allure
from pages.index_page import IndexPage
from pages.personal_account_page import PersonalAccountPage
from data.data_url import *

class TestPasswordRecovery:
    # @allure.title('Проверяем переход на страницу восстановления пароля по кнопке «Восстановить пароль')
    # def test_click_recovery_password(self, fixture_get_driver):
    #     driver = fixture_get_driver
    #     page1 = IndexPage(driver, index_url)
    #     page2 = PersonalAccountPage(driver, personal_account_url)
    #     page1.p_open_index_page()
    #     page1.p_click_personal_account_page()
    #     page2.p_click_password_recovery()
    #
    #     current_url = driver.current_url
    #     assert "/forgot-password" in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"

    # @allure.title('Проверяем ввод почты и клик по кнопке «Восстановить»')
    # def test_click_recovery_password(self, fixture_get_driver):
    #     driver = fixture_get_driver
    #     page1 = IndexPage(driver, index_url)
    #     page2 = PersonalAccountPage(driver, personal_account_url)
    #     page1.p_open_index_page()
    #     page1.p_click_personal_account_page()
    #     page2.p_click_password_recovery()
    #     page2.p_email_recovery()
    #     page2.p_click_button_recovery()
    #     time.sleep(3)
    #
    #     current_url = driver.current_url
    #     assert "/reset-password" in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.title('Проверяем, что клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его»')
    def test_click_recovery_password(self, fixture_get_driver):
        driver = fixture_get_driver
        page1 = IndexPage(driver, index_url)
        page2 = PersonalAccountPage(driver, personal_account_url)

        page1.p_open_index_page()
        page1.p_click_personal_account_page()

        page2.p_enter_password()
        page2.p_click_eye()
        password_type = page2.p_get_attribute_type()
        assert password_type == "text", "Пароль должен быть видимым после нажатия на иконку"

        page2.p_click_eye()
        password_type = page2.p_get_attribute_type()
        assert password_type == "password", "Пароль должен быть невидимым после нажатия на иконку"
