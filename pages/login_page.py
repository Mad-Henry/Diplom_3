import allure
from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as LPL


class LoginPage(BasePage):


    @allure.step("Переход по 'Ввосстановления пароля'")
    def click_on_restore_psswrd_link(self):
        self.click(LPL.RESTORE_PASSWORD_LINK)


    @allure.step("Авторизация пользователя")
    def login_in_to_a_profile(self, email, psswrd):
        self.send_keys(LPL.EMAIL_FIELD, email)
        self.send_keys(LPL.PASSWORD_FIELD, psswrd)
        self.forse_click(LPL.ENTER_BUTTON)
        self.wait_for_invisibility(LPL.ENTER_BUTTON)
        