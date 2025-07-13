import allure
from pages.base_page import BasePage
from locators.constructor_page_locators import ConstructorPageLocators


class ConstructorPage(BasePage):


    @allure.step("Выбор 'Краторная булка N-200i'")
    def set_bun(self):
        self.click(ConstructorPageLocators.INGREDIENT_BUN)


    @allure.step("Проверка появления 'Детали ингредиента'")
    def check_for_details_window(self):
        return self.wait_for_presence(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)


    @allure.step("Закрытие 'Детали ингредиента'")
    def close_details_window(self):
        self.click(ConstructorPageLocators.MODAL_CLOSE_BUTTON)
        return self.wait_for_invisibility(ConstructorPageLocators.INGREDIENT_DETAILS_MODAL_TITLE)


    @allure.step("Добавление булки в корзину")
    def add_bun_to_order(self):
        move_from = self.find(ConstructorPageLocators.INGREDIENT_BUN)
        move_to = self.find(ConstructorPageLocators.ORDER_CART)
        self.drag_and_drop_element(move_from, move_to)


    @allure.step("Проверка счетчика ингридиентов")
    def ingredients_counter(self):
        return self.find(ConstructorPageLocators.INGREDIENT_COUNTER).text


    @allure.step("Клик 'Создание заказа'")
    def create_an_order(self):
        self.wait_until_clickable(ConstructorPageLocators.INGREDIENT_BUN)
        bun = self.find(ConstructorPageLocators.INGREDIENT_BUN)
        cart = self.find(ConstructorPageLocators.ORDER_CART)
        self.drag_and_drop_element(bun, cart)
        souse = self.find(ConstructorPageLocators.INGREDIENT_SAUCE)
        self.drag_and_drop_element(souse, cart)
        adding_ellement = self.find(ConstructorPageLocators.INGREDIENT_FILLING)
        self.drag_and_drop_element(adding_ellement, cart)
        self.forse_click(ConstructorPageLocators.ORDER_CREATE_BUTTON)
        self.wait_until_clickable(ConstructorPageLocators.ORDER_MODAL_FRAME)
        self.wait_for_invisibility(ConstructorPageLocators.DEFAULT_ORDER_NUMBER)
        self.wait_for_presence(ConstructorPageLocators.ORDER_IS_PREPARING_TEXT)
        order_num = self.wait_until_clickable(ConstructorPageLocators.REAL_ORDER_NUMBER).text
        self.forse_click(ConstructorPageLocators.CLOSE_ORDER_MENU_BUTTON)
        return order_num


    @allure.step("Ожидание появления созданного заказа")
    def order_confirmation_is_presence(self):
        return self.wait_for_presence(ConstructorPageLocators.ORDER_IS_PREPARING_TEXT)


    @allure.step("Клик 'Лента Заказов'")
    def click_orders_feed_button(self):
        self.forse_click(ConstructorPageLocators.ORDER_FEED_BUTTON)
