import allure
from locators import IndexPageLocators
from pages.base_page import BasePage

from selenium.webdriver.common.by import By


class IndexPage(BasePage):
    def __init__(self, driver, index_url):
        super().__init__(driver)
        self.index_url = index_url
        self.locators = IndexPageLocators()

    @allure.step("Открываем главную страницу")
    def p_open_index_page(self):
        self.f_open_page(self.index_url)

    @allure.step("Кликаем на кнопку Личный кабинет")
    def p_click_personal_account_page(self):
        self.f_click_element(self.locators.PERSONAL_ACCOUNT)

    @allure.step("Кликаем на кнопку Личный кабинет, пользователь авторизован")
    def p_click_personal_account_page_auth(self):
        self.f_click_element(self.locators.PERSONAL_ACCOUNT_AUTH)

    @allure.step("Кликаем на кнопку 'Лента Заказов'")
    def p_click_lenta_zakazov_button(self):
        self.f_click_element(self.locators.LENTA_ZAKAZOV_BUTTON)

    @allure.step("Кликаем на кнопку 'Конструктор'")
    def p_click_konstruktor_button(self):
        self.f_wait_inv_element(self.locators.MODAL_WINDOW)
        self.f_click_element(self.locators.KONSTRUKTOR_BUTTON)

    @allure.step("Ищем все ингредиенты")
    def p_find_ingredients(self):
        ingredients = self.f_find_ingredients(self.locators.ALL_INGREDIENTS)
        return ingredients

    @allure.step("Кликаем на случайно выбранный ингредиент")
    def p_click_ingredient(self, random_ingredient):
        self.f_click_ingredient(random_ingredient)

    @allure.step("Кликаем на первый ингредиент")
    def p_click_first_ingredient(self):
        self.f_click_first_ingredient(self.locators.FIRST_INGREDIENT)

    @allure.step('Проверяем заголовок модального окна')
    def p_check_modal_window_header(self):
        header = self.f_wait_for_element(self.locators.MODAL_WINDOW_HEADER_LOCATOR)
        return header.text

    @allure.step('Кликаем на кнопку закрытия модального окна')
    def p_click_button_for_close_modal_window(self):
       self.f_click_button_for_close_modal_window(self.locators.MODAL_WINDOW_CLOSE_BUTTON)

    @allure.step('Проверяем закрытие модального окна')
    def p_check_modal_window_close(self):
        is_modal_closed = self.f_check_modal_window_close(self.locators.MODAL_WINDOW)
        return is_modal_closed

    def p_wait_page(self, page):
        self.f_wait_page(page)

    @allure.step('Переносим ингредиент в корзину')
    def p_drag_and_drop_ingredient_to_basket(self):
        initial_counter, updated_counter = self.f_drag_and_drop_ingredient_to_basket(self.locators.BASKET_INGREDIENT, self.locators.BASKET, self.locators.COUNTER)
        return initial_counter, updated_counter

    @allure.step('Проверка, что пользователь может сделать заказ')
    def p_check_button_submit_order(self):
        result = self.f_check_button_submit_order(self.locators.ORDER_BUTTON)
        return result








