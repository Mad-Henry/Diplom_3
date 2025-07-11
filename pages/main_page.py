import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):


    @allure.step("Нажатие 'Войти в аккаунт'")
    def click_login_button(self):
        self.click(MainPageLocators.LOGIN_BUTTON)


    @allure.step("Нажатие 'Войти в Личный кабинет'")
    def click_profile_button(self):
        self.forse_click(MainPageLocators.PROFILE_BUTTON)


    @allure.step("Вход в личный кабинет после авторизации")
    def move_in_profile_after_auth(self):
        self.forse_click(MainPageLocators.PROFILE_BUTTON)


    @allure.step("Нажатие 'Конструктор'")
    def click_to_constructor_button(self):
        self.click(MainPageLocators.CONSTRUCTOR_BUTTON)


    @allure.step("Нажатие 'Лента Заказов'")
    def click_to_orders_feed_button(self):
        self.forse_click(MainPageLocators.ORDER_FEED_BUTTON)

