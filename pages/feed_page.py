import allure
from locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def __init__(self, driver, feed_url):
        super().__init__(driver)
        self.feed_url = feed_url
        self.locators = FeedPageLocators()

    @allure.step("Кликаем на кнопку 'Лента Заказов'")
    def p_click_lenta_zakazov_button(self):
        self.f_click_element(self.locators.LENTA_ZAKAZOV_BUTTON)

    @allure.step("Кликаем на случайно выбранный заказ")
    def p_click_order(self):
        selected_order, order_title = self.f_click_order(self.locators.ORDERS_LIST, self.locators.ORDER_TITLE, self.locators.ORDER_LINK)
        return selected_order, order_title

    @allure.step("Проверяем, что заголовок заказа совпадает с заголовком в открытом окне")
    def p_check_open_details(self, selected_order):
        page_title = self.f_check_open_details(self.locators.ORDER_NAME, selected_order)
        return page_title

    @allure.step("Получаем список всех заказов")
    def p_get_recent_orders(self):
        order_elements = self.f_get_recent_orders(self.locators.ORDER_ITEMS)
        order_numbers = []
        for item in order_elements:
            order_number = self.f_get_number_of_recent_order(self.locators.ORDER_NUMBER, item)
            order_numbers.append(order_number)
        return order_numbers

    @allure.title('Кликаем на кнопку Конструктор')
    def p_click_konstruktor_button(self):
        self.f_click_element(self.locators.KONSTRUKTOR_BUTTON)


    @allure.title('Считаем общее количество заказов')
    def p_get_total_orders_count(self):
        counter_element = self.f_get_total_orders_count(self.locators.TOTAL_ORDERS_COUNTER)
        return counter_element

    @allure.title('Считаем общее количество заказов за день')
    def p_get_total_orders_count_for_day(self):
        counter_element = self.f_get_total_orders_count(self.locators.TOTAL_ORDERS_COUNTER_FOR_DAY)
        return counter_element

    @allure.title('Cобираем все заказы в работе')
    def p_check_is_order_in_progress(self):
        order_numbers = self.f_check_is_order_in_progress(self.locators.ORDERS_IN_PROGRESS)
        return order_numbers

    @allure.step('Ждем загрузки страницы')
    def p_wait_page(self, url):
        self.f_wait_page(url)