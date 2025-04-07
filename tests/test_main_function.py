import allure
import random

from pages.index_page import IndexPage
from pages.personal_account_page import PersonalAccountPage
from data.data_url import *



class TestMainFunction:
    @allure.title('Проверяем переход по клику на Конструктор')
    def test_click_konstruktor_button(self, fixture_get_driver):
        driver = fixture_get_driver
        page1 = IndexPage(driver, index_url)
        page1.p_open_index_page()
        page1.p_click_lenta_zakazov_button()
        page1.p_click_konstruktor_button()
        current_url = driver.current_url
        assert index_url in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.title('Проверяем переход по клику на Ленту заказов`')
    def test_click_konstruktor_button(self, fixture_get_driver):
        driver = fixture_get_driver
        page1 = IndexPage(driver, index_url)
        page1.p_open_index_page()
        page1.p_click_lenta_zakazov_button()

        current_url = driver.current_url
        assert "/feed" in current_url, f"Ожидался URL: {expected_url}, но получен: {current_url}"

    @allure.title('Проверяем, что при клике на ингредиент, появится всплывающее окно с деталями')
    def test_modal_window_of_ingredients(self, fixture_get_driver):
        driver = fixture_get_driver
        page1 = IndexPage(driver, index_url)
        page1.p_open_index_page()
        ingredients = page1.p_find_ingredients()
        assert len(ingredients) > 0, "Список ингредиентов пуст"

        random_ingredient = random.choice(ingredients)
        page1.p_click_ingredient(random_ingredient)
        modal_title = page1.p_check_modal_window_header()

        assert modal_title == "Детали ингредиента", "Заголовок всплывающего окна не соответствует ожидаемому"

    @allure.title('Проверяем закрытие модального окна по клику на крестик')
    def test_close_modal_window_of_ingredients(self, fixture_get_driver):
        driver = fixture_get_driver
        page1 = IndexPage(driver, index_url)
        page1.p_open_index_page()
        page1.p_click_first_ingredient()
        page1.p_click_button_for_close_modal_window()
        is_modal_closed = page1.p_check_modal_window_close()
        assert is_modal_closed is True, "Модальное окно не закрылось"

    @allure.title('Проверяем, что счетчик ингредиента увеличивается при переносе его в корзину')
    def test_drag_and_drop_ingredient_increase_counter(self, fixture_get_driver):
        driver = fixture_get_driver
        page1 = IndexPage(driver, index_url)
        page1.p_open_index_page()
        initial_counter, updated_counter = page1.p_drag_and_drop_ingredient_to_basket()
        assert updated_counter == initial_counter + 1, \
            f"Ожидалось, что счетчик увеличится на 1. Было: {initial_counter}, стало: {updated_counter}"

    @allure.title('Проверяем, что зарегистрированный пользователь может разместить заказ')
    def test_user_can_place_order(self, fixture_get_driver):
        driver = fixture_get_driver
        page1 = IndexPage(driver, index_url)
        page2 = PersonalAccountPage(driver, personal_account_url)

        page1.p_open_index_page()
        time.sleep(2)
        page1.p_click_personal_account_page()
        page2.p_login_user()
        page1.p_drag_and_drop_ingredient_to_basket()
        result = page1.p_check_button_submit_order()
        assert result is True, "Пользователь не смог сделать заказ"



