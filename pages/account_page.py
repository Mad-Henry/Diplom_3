import allure
from pages.base_page import BasePage
from locators.account_page_locators import AccountPageLocators


class AccountPage(BasePage):


    @allure.step("Клик по 'История заказов'")
    def click_on_order_history_menu(self):
        self.click(AccountPageLocators.ORDER_HISTORY_LINK)


    @allure.title("Клик по 'Выход из аккаунта'")
    def click_logout_from_account(self):
        self.click(AccountPageLocators.LOGOUT_BUTTON)
        self.wait_for_invisibility(AccountPageLocators.LOGOUT_BUTTON)
