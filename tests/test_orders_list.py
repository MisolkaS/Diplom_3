import allure
from pages.index_page import IndexPage
from pages.personal_account_page import PersonalAccountPage
from pages.feed_page import FeedPage
from data.data_url import *
from data.data_user import *

class TestOrdersList:
    @allure.title('Проверяем, что при клике на заказ открывается всплывающее окно с деталями')
    def test_click_on_order_open_window_details(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        feed_page = FeedPage(driver, feed_url)

        index_page.p_open_index_page()
        index_page.p_click_lenta_zakazov_button()

        selected_order, order_title = feed_page.p_click_order()
        page_title = feed_page.p_check_open_details(selected_order)

        with allure.step('Всплывающее окно с деталями открылось'):
            assert order_title == page_title, f"Ожидался URL: {order_title}, но получен: {page_title}"

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_appear_in_order_feed(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)
        feed_page = FeedPage(driver, feed_url)

        index_page.p_open_index_page()
        index_page.p_click_personal_account_page()
        personal_account_page.p_login_user(registration_data['email'], registration_data['password'])

        index_page.p_create_new_order()
        index_page.p_click_button_for_close_modal_window()

        index_page.p_click_personal_account_page()
        personal_account_page.p_click_orders_history()

        order_numbers = personal_account_page.p_count_user_orders()

        feed_page.p_click_lenta_zakazov_button()
        feed_page.p_wait_page(feed_url)
        all_order_numbers = feed_page.p_get_recent_orders()

        found_numbers = set(order_numbers).intersection(all_order_numbers)

        with allure.step('Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»'):
            assert found_numbers, "Ни один из номеров заказов не найден в общем списке"

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_completed_orders_counter(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)
        feed_page = FeedPage(driver, feed_url)
        index_page.p_open_index_page()

        index_page.p_click_personal_account_page()
        personal_account_page.p_login_user(registration_data['email'], registration_data['password'])

        index_page.p_click_lenta_zakazov_button()
        initial_count = feed_page.p_get_total_orders_count()
        feed_page.p_click_konstruktor_button()
        index_page.p_create_new_order()

        index_page.p_click_button_for_close_modal_window()
        index_page.p_click_lenta_zakazov_button()
        updated_count = feed_page.p_get_total_orders_count()

        with allure.step('Счётчик Выполнено за всё время увеличился'):
            assert updated_count > initial_count, f"Счётчик не увеличился. Было: {initial_count}, стало: {updated_count}"
            allure.attach(f"Изначальное значение счётчика: {initial_count}",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"Новое значение счётчика: {updated_count}",
                          attachment_type=allure.attachment_type.TEXT)

    @allure.title('Проверяем, что при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_completed_orders_counter_for_day(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)
        feed_page = FeedPage(driver, feed_url)
        index_page.p_open_index_page()

        index_page.p_click_personal_account_page()
        personal_account_page.p_login_user(registration_data['email'], registration_data['password'])

        index_page.p_click_lenta_zakazov_button()
        initial_count = feed_page.p_get_total_orders_count_for_day()
        feed_page.p_click_konstruktor_button()
        index_page.p_create_new_order()

        index_page.p_click_button_for_close_modal_window()
        index_page.p_click_lenta_zakazov_button()
        updated_count = feed_page.p_get_total_orders_count_for_day()

        with allure.step('Счётчик Выполнено за сегодня увеличился'):
            assert updated_count > initial_count, f"Счётчик не увеличился. Было: {initial_count}, стало: {updated_count}"
            allure.attach(f"Изначальное значение счётчика: {initial_count}",
                          attachment_type=allure.attachment_type.TEXT)
            allure.attach(f"Новое значение счётчика: {updated_count}",
                          attachment_type=allure.attachment_type.TEXT)


    @allure.title('Проверяем, что после оформления заказа его номер появляется в разделе В работе')
    def test_new_order_is_in_progress(self, fixture_get_driver):
        driver = fixture_get_driver
        index_page = IndexPage(driver, index_url)
        personal_account_page = PersonalAccountPage(driver, personal_account_url)
        feed_page = FeedPage(driver, feed_url)
        index_page.p_open_index_page()

        index_page.p_click_personal_account_page()
        personal_account_page.p_login_user(registration_data['email'], registration_data['password'])

        index_page.p_create_new_order()

        order_number = index_page.p_get_order_number()
        index_page.p_click_button_for_close_modal_window()
        index_page.p_click_lenta_zakazov_button()
        order_numbers = feed_page.p_check_is_order_in_progress()

        with allure.step('Номер заказа появился в разделе В работе'):
            assert f"0{order_number}" in order_numbers, f"Номер заказа {order_number} отсутствует в списке."

