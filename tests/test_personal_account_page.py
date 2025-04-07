import time

import allure

from pages.index_page import IndexPage
from pages.personal_account_page import PersonalAccountPage
from data.data_url import *

class TestLoginPage:
    # @allure.title('Проверяем переход по клику на Личный кабинет не авторизованного пользователя')
    # def test_click_on_login_page(self, fixture_get_driver):
    #     driver = fixture_get_driver
    #     page1 = IndexPage(driver, index_url)
    #     page1.p_open_index_page()
    #     page1.p_click_personal_account_page()
    #     current_url = driver.current_url
    #     assert "login" in current_url, f"Ожидался URL, содержащий 'login', но получен: {current_url}"

    # @allure.title('Проверяем переход в раздел история заказов')
    # def test_click_on_login_page(self, fixture_get_driver):
    #     driver = fixture_get_driver
    #     page1 = IndexPage(driver, index_url)
    #     page2 = PersonalAccountPage(driver, personal_account_url)
    #
    #     page1.p_open_index_page()
    #     time.sleep(2)
    #     page1.p_click_personal_account_page()
    #     page2.p_login_user()
    #     time.sleep(2)
    #     page1.p_click_personal_account_page_auth()
    #     page2.p_click_orders_history()
    #     current_url = driver.current_url
    #     assert "order-history" in current_url, f"Ожидался URL, содержащий 'history', но получен: {current_url}"


    @allure.title('Проверяем выход из аккаунта')
    def test_click_on_login_page(self, fixture_get_driver):
        driver = fixture_get_driver
        page1 = IndexPage(driver, index_url)
        page2 = PersonalAccountPage(driver, personal_account_url)

        page1.p_open_index_page()
        time.sleep(2)
        page1.p_click_personal_account_page()
        page2.p_login_user()
        time.sleep(2)
        page1.p_click_personal_account_page_auth()
        page2.p_click_logout()
        time.sleep(2)
        current_url = driver.current_url

        assert "login" in current_url, f"Ожидался URL, содержащий 'login', но получен: {current_url}"


