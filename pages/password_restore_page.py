import allure
from pages.base_page import BasePage
from locators.password_restore_page_locators import RestorePasswordPageLocators as RPP
from helpers import HelpersMethods as HM


class PasswordRestorePage(BasePage):


    @allure.step("Ввод email и подтверждение восстановления пароля")
    def enter_email_and_confirm(self):
        self.click(RPP.EMAIL_FIELD)
        self.send_keys(RPP.EMAIL_FIELD, HM.generate_email())
        self.click(RPP.PSSWRD_RESTORE_BUTTON)
        self.wait_for_presence(RPP.NEW_PSSWRD_CONFIRM_BUTTON)


    @allure.step("Нажатие на иконку отображения пароля")
    def click_shows_password_icon(self):
        self.click_on_element(RPP.PSSWRD_SHOW_TOGGLE)


    @allure.step("Проверка, что поле пароля активно")
    def check_is_password_field_active(self):
        return self.check_elements_displaying(RPP.PSSORD_FIELD_IS_ACTIVE)
    