import allure
from locators import FeedPageLocators
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


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
        selected_order, order_title = self.f_click_order()
        return selected_order, order_title

    @allure.step("Проверяем, что заголовок заказа совпадает с заголовком в открытом окне")
    def p_check_open_details(self, selected_order):
        page_title = self.f_check_open_details(selected_order)
        return page_title