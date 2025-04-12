import allure

from pages.index_page import IndexPage
from pages.personal_account_page import PersonalAccountPage
from data.data_url import *

class TestLoginPage:
    @allure.title('Проверяем переход по клику на Личный кабинет не авторизованного пользователя')
    def test_click_on_login_page(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)

        index_page.p_open_index_page()
        index_page.p_click_personal_account_page()

        current_url = driver.current_url
        with allure.step('Перешли на Личный кабинет не авторизованного пользователя'):
            assert "login" in current_url, f"Ожидался URL, содержащий 'login', но получен: {current_url}"

    @allure.title('Проверяем переход в раздел история заказов')
    def test_navigate_to_order_history(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)
        index_page.p_open_index_page()

        index_page.p_click_personal_account_page()
        personal_account_page.p_login_user()

        index_page.p_click_personal_account_page_auth()
        personal_account_page.p_click_orders_history()

        current_url = driver.current_url
        with allure.step('Перешли в раздел история заказов'):
            assert "order-history" in current_url, f"Ожидался URL, содержащий 'history', но получен: {current_url}"


    @allure.title('Проверяем выход из аккаунта')
    def test_user_can_logout(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)
        index_page.p_open_index_page()

        index_page.p_click_personal_account_page()
        personal_account_page.p_login_user()

        index_page.p_click_personal_account_page_auth()
        personal_account_page.p_click_logout()
        personal_account_page.p_wait_page(personal_account_url)
        current_url = driver.current_url

        with allure.step('Вышли из аккаунта'):
           assert "login" in current_url, f"Ожидался URL, содержащий 'login', но получен: {current_url}"


