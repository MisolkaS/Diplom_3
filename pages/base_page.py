from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
from selenium.common.exceptions import TimeoutException
import random

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def f_open_page(self, page_url):
        self.driver.get(page_url)

    def f_wait_page(self, page):
        WebDriverWait(self.driver, 20).until(
            EC.url_to_be({page})
        )

    def f_get_attribute_type(self, locator):
        password_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )
        input_type = password_field.get_attribute("type")
        return input_type

    def f_click_eye(self, locator):
        #eye_icon = self.driver.find_element(*locator)
        #self.driver.execute_script("arguments[0].click();", eye_icon)
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        element.click()


    def f_wait_inv_element (self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((locator))
        )
    def f_click_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        element.click()

    def f_find_ingredients(self, locator):
        ingredients = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(locator))
        return ingredients

    def f_click_ingredient(self, random_ingredient):
        WebDriverWait(self.driver, 20).until(EC.visibility_of(random_ingredient))
        self.driver.execute_script("arguments[0].scrollIntoView();", random_ingredient)
        random_ingredient.click()

    def f_wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def f_click_button_for_close_modal_window(self, locator):
        close_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        close_button.click()


    def f_check_modal_window_close(self, locator):

        is_modal_closed = WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(locator)
        )
        return is_modal_closed


    def f_click_first_ingredient(self, locator):
        ingredient_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].click();", ingredient_element)

    def f_wait_and_send_keys(self, locator, keys):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )
        element.send_keys(keys)

    def f_check_button_submit_order(self, locator):
        elements = self.driver.find_elements(*locator)
        if elements and elements[0].is_displayed():
            return True
        return False

    def f_drag_and_drop_ingredient_to_basket(self, ingredient_locator, basket_locator, counter_locator):
        ingredient = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ingredient_locator)
        )
        counter = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(counter_locator)
        )
        initial_counter = counter.text
        initial_counter_value = int(initial_counter) if initial_counter else 0

        self.driver.execute_script("arguments[0].scrollIntoView();", ingredient)

        basket = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(basket_locator)
        )

        actions = ActionChains(self.driver)
        actions.click_and_hold(ingredient).move_to_element(basket).release().perform()

        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(counter_locator, str(initial_counter_value + 1))
        )

        updated_counter = self.driver.find_element(*counter_locator).text
        return int(initial_counter), int(updated_counter)


    # def f_click_order(self):
    #     orders = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_all_elements_located(self.ORDERS_LIST)
    #         )
    #     selected_order = random.choice(orders[:10])
    #     selected_order_index = orders.index(selected_order) + 1
    #     self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
    #                               selected_order)
    #     order_title = selected_order.find_element(*self.ORDER_TITLE).text
    #     order_link = selected_order.find_element(*self.ORDER_LINK)
    #     self.driver.execute_script("arguments[0].click();", order_link)
    #     return selected_order_index, order_title
    #
    # def f_check_open_details(self, selected_order):
    #     locator = (By.XPATH, f"(//h2[contains(@class, 'text text_type_main-medium mb-2')])[{selected_order}]")
    #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
    #     h2_text = element.text
    #     print(f"Текст в h2 (элемент {selected_order}): {h2_text}")
    #     return h2_text



