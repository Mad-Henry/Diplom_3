import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    

    @allure.step('Выбор последнего созданного заказа')
    def select_last_order(self):
        self.click(OrderFeedPageLocators.ORDER_IN_FEED_LINK)


    @allure.step('Проверка появления окна при выборе заказа')
    def check_for_order_windows_visability(self):
        return self.wait_for_presence(OrderFeedPageLocators.ORDER_MODAL_CONTENTS_TITLE)
    

    @allure.step("Поиск заказа в ленте")
    def find_order_in_order_list(self, order_number):
        return self.wait_until_clickable(OrderFeedPageLocators.get_order_in_order_feed(order_number))
    

    @allure.step("Клик по 'Конструктор'")
    def click_on_to_constructor_button(self):
        self.click(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)


    @allure.step("Значение 'Выполнено за всё время'")
    def get_number_of_total_orders(self):
        self.wait_until_clickable(OrderFeedPageLocators.COMPLETE_ORDERS_TOTAL_COUNTER)
        return self.wait_for_presence(OrderFeedPageLocators.COMPLETE_ORDERS_TOTAL_COUNTER).text


    @allure.step("Значени 'Выполнено за сегодня'")
    def get_number_of_today_orders(self):
        self.wait_until_clickable(OrderFeedPageLocators.COMPLETE_ORDERS_TODAY_COUNTER)
        return self.wait_for_presence(OrderFeedPageLocators.COMPLETE_ORDERS_TODAY_COUNTER).text


    @allure.step("Значение 'В работе'")
    def get_number_in_work_list(self):
        self.wait_until_clickable(OrderFeedPageLocators.ORDER_NUMBER_IN_WORK)
        return self.wait_for_presence(OrderFeedPageLocators.ORDER_NUMBER_IN_WORK).text
    