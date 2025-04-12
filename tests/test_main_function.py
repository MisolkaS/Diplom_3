import allure
import random

from pages.index_page import IndexPage
from pages.personal_account_page import PersonalAccountPage
from data.data_url import *

class TestMainFunction:
    @allure.title('Проверяем переход по клику на Конструктор')
    def test_click_konstruktor_button(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        index_page.p_open_index_page()
        index_page.p_click_lenta_zakazov_button()
        index_page.p_click_konstruktor_button()
        current_url = driver.current_url
        with allure.step('Переход по клику на Конструктор'):
            assert index_url in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.title('Проверяем переход по клику на Ленту заказов')
    def test_click_list_orders(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        index_page.p_open_index_page()
        index_page.p_click_lenta_zakazov_button()

        current_url = driver.current_url
        with allure.step('Переход по клику на Ленту заказов'):
            assert "/feed" in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.title('Проверяем, что при клике на ингредиент, появится всплывающее окно с деталями')
    def test_modal_window_of_ingredients(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        index_page.p_open_index_page()
        ingredients = index_page.p_find_ingredients()
        assert len(ingredients) > 0, "Список ингредиентов пуст"

        random_ingredient = random.choice(ingredients)
        index_page.p_click_ingredient(random_ingredient)
        modal_title = index_page.p_check_modal_window_header()
        with allure.step('При клике на ингредиент, появляется всплывающее окно с деталями'):
            assert modal_title == "Детали ингредиента", "Заголовок всплывающего окна не соответствует ожидаемому"

    @allure.title('Проверяем закрытие модального окна по клику на крестик')
    def test_close_modal_window_of_ingredients(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        index_page.p_open_index_page()
        index_page.p_click_first_ingredient()
        index_page.p_click_button_for_close_modal_window()
        is_modal_closed = index_page.p_check_modal_window_close()
        with allure.step('Модальное окно закрылось'):
            assert is_modal_closed is True, "Модальное окно не закрылось"

    @allure.title('Проверяем, что счетчик ингредиента увеличивается при переносе его в корзину')
    def test_drag_and_drop_ingredient_increase_counter(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        index_page.p_open_index_page()
        initial_counter, updated_counter = index_page.p_drag_and_drop_ingredient_to_basket()
        with allure.step('Счетчик ингредиента увеличился'):
            assert updated_counter == initial_counter + 1, \
            f"Ожидалось, что счетчик увеличится на 1. Было: {initial_counter}, стало: {updated_counter}"

    @allure.title('Проверяем, что зарегистрированный пользователь может разместить заказ')
    def test_user_can_place_order(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)

        index_page.p_open_index_page()

        index_page.p_click_personal_account_page()
        personal_account_page.p_login_user()
        index_page.p_drag_and_drop_ingredient_to_basket()
        result = index_page.p_check_button_submit_order()
        with allure.step('Зарегистрированный пользователь разместил заказ'):
            assert result is True, "Пользователь не смог сделать заказ"



