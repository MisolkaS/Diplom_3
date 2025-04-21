from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure
import random

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу")
    def f_open_page(self, page_url):
        self.driver.get(page_url)

    @allure.step("Ожидаем открытие страницы")
    def f_wait_page(self, page):
        WebDriverWait(self.driver, 20).until(
            EC.url_to_be(page)
        )

    @allure.step("Получаем тип поля Пароль")
    def f_get_attribute_type(self, locator):
        password_field = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )
        input_type = password_field.get_attribute("type")
        return input_type

    @allure.step("Нажимаем на кнопку скрыть/показать пароль")
    def f_click_eye(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ждем исчезновения элемента")
    def f_wait_inv_element (self, locator):
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((locator))
        )

    @allure.step("Кликаем на элемент")
    def f_click_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        element.click()

    @allure.step("Ждем загрузки ингредиентов")
    def f_find_ingredients(self, locator):
        ingredients = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located(locator))
        return ingredients

    @allure.step("Кликаем на случайный ингредиент")
    def f_click_ingredient(self, random_ingredient):
        WebDriverWait(self.driver, 20).until(EC.visibility_of(random_ingredient))
        self.driver.execute_script("arguments[0].scrollIntoView();", random_ingredient)
        random_ingredient.click()

    @allure.step("Ждем загрузки элемента")
    def f_wait_for_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Закрываем модальное окно")
    def f_click_button_for_close_modal_window(self, locator, loading_locator):
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(loading_locator)
        )
        close_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator)
        )
        close_button.click()

    @allure.step("Проверяем закрытие модального окна")
    def f_check_modal_window_close(self, locator):
        is_modal_closed = WebDriverWait(self.driver, 20).until(
            EC.invisibility_of_element_located(locator)
        )
        return is_modal_closed


    @allure.step("Кликаем на ингредиент")
    def f_click_first_ingredient(self, locator):
        ingredient_element = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable(locator)
        )
        self.driver.execute_script("arguments[0].click();", ingredient_element)

    @allure.step("Заполняем поле")
    def f_wait_and_send_keys(self, locator, keys):
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(locator)
        )
        element.send_keys(keys)

    @allure.step("Проверка кнопки Заказать")
    def f_check_button_submit_order(self, locator):
        elements = self.driver.find_elements(*locator)
        if elements and elements[0].is_displayed():
            return True
        return False

    @allure.step("Ждем загрузки элементов")
    def f_wait_any_elements(self, locator):
        elements = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(locator))
        return elements

    @allure.step("Считываем текст элемента")
    def f_wait_any_elements_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        result = element.text
        return result

    @allure.step("Скроллимся к элементу")
    def f_scroll_to_element(self, ingredient_locator):
        ingredient = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ingredient_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", ingredient)

    @allure.step("Переносим ингредиент в корзину")
    def f_drag_and_drop_ingredient_to_basket(self, ingredient_locator, basket_locator):
        ingredient = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(ingredient_locator)
        )
        basket = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(basket_locator)
        )
        actions = ActionChains(self.driver)
        actions.click_and_hold(ingredient).move_to_element(basket).release().perform()

    @allure.step("Считываем текст элемента после переноса")
    def f_check_counter(self, counter_locator, initial_counter_value):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(counter_locator, str(initial_counter_value + 1))
        )
        updated_counter = self.driver.find_element(*counter_locator).text
        return updated_counter

    @allure.step("Получаем общее количество заказов")
    def f_get_total_orders_count(self, locator):
        counter_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(locator)
            )
        return int(counter_element.text)

    @allure.step("Получаем количество заказов")
    def f_get_order_number(self, locator, loading_locator):
        WebDriverWait(self.driver, 30).until(
            EC.invisibility_of_element_located(loading_locator)
        )
        counter_element = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(locator)
            )
        return counter_element.text

    @allure.step("Получаем список заказов")
    def f_get_recent_orders(self, order_items_locator):
        order_elements = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(order_items_locator)
        )
        return order_elements

    @allure.step("Получаем номер заказа")
    def f_get_number_of_recent_order(self, order_number_locator, item):
        element = WebDriverWait(item, 30).until(EC.presence_of_element_located(order_number_locator))
        return element.text


    @allure.step("Получаем список заказов в работе")
    def f_check_is_order_in_progress(self, locator):
        WebDriverWait(self.driver, 30).until(
                EC.presence_of_all_elements_located(locator)
            )
        order_number_elements = self.driver.find_elements(*locator)
        order_numbers = [element.text for element in order_number_elements]
        return order_numbers

    @allure.step("Получаем заголовок и номер случайного выбранного заказа")
    def f_click_order(self, locator_orders_list, locator_order_title, locator_order_link):
        orders = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(locator_orders_list)
            )
        selected_order = random.choice(orders[:10])
        selected_order_index = orders.index(selected_order) + 1
        self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                                  selected_order)
        order_title = selected_order.find_element(*locator_order_title).text
        order_link = selected_order.find_element(*locator_order_link)
        self.driver.execute_script("arguments[0].click();", order_link)
        return selected_order_index, order_title

    @allure.step("Получаем заголовок модального окна")
    def f_check_open_details(self, locator, selected_order):
        locator = (locator[0], f"({locator[1]})[{selected_order}]")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        h2_text = element.text
        return h2_text

    @allure.step("Получаем URL текущей страницы")
    def f_get_current_url(self):
        current_url = self.driver.current_url
        return current_url