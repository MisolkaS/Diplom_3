import time

import allure
import random

from pages.index_page import IndexPage
from pages.personal_account_page import PersonalAccountPage
from pages.feed_page import FeedPage
from data.data_url import *


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains




class TestOrdersList:
    # @allure.title('Проверяем, что при клике на заказ открывается всплывающее окно с деталями')
    # def test_click_on_order_open_window_details(self, fixture_get_driver):
    #     driver = fixture_get_driver
    #     page1 = IndexPage(driver, index_url)
    #     page1.p_open_index_page()
    #     page1.p_click_lenta_zakazov_button()
    #     page2 = FeedPage(driver, feed_url)
    #     selected_order, order_title = page2.p_click_order()
    #     page_title = page2.p_check_open_details(selected_order)
    #     assert order_title == page_title, f"Ожидался URL: {order_title}, но получен: {page_title}"

    @allure.title('Проверяем, что заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_click_on_order_open_window_details(self, fixture_get_driver):
        driver = fixture_get_driver
        page1 = IndexPage(driver, index_url)
        page2 = PersonalAccountPage(driver, personal_account_url)
        page3 = FeedPage(driver, feed_url)
        page1.p_open_index_page()

        page1.p_click_personal_account_page()
        time.sleep(3)

        page2.p_login_user()
        time.sleep(3)

        page1.p_click_personal_account_page()
        page2.p_click_orders_history()

        wait = WebDriverWait(driver, 10)
        order_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, 'text_type_digits-default')]")))


        order_numbers = [element.text for element in order_elements]
        print(f"{order_numbers}")

        page3.p_click_lenta_zakazov_button()
        wait = WebDriverWait(driver, 10)
        order_items = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "OrderHistory_listItem__2x95r")))


        all_order_numbers = []
        for item in order_items:
            order_number = item.find_element(By.CLASS_NAME, "text_type_digits-default").text
            all_order_numbers.append(order_number)


        print(all_order_numbers)
        assert set(order_numbers).issubset(all_order_numbers)
