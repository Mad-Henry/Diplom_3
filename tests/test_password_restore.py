import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.password_restore_page import PasswordRestorePage
from URLs import BASE_URL, PASSWORD_RESTORE_URL, PASSWORD_RESET_URL


@allure.story("Проверки 'Восстановление пароля'")
class TestPasswordRestore:


    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_open_psswrd_recovery_page(self, browser):
        page = MainPage(browser)
        page.open()
        page.click_login_button()
        page = LoginPage(browser)
        page.click_on_restore_psswrd_link()
        url_4_assert = BASE_URL + PASSWORD_RESTORE_URL
        assert page.current_url() == url_4_assert, \
            f"Текущий URL {page.current_url()}"


    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_input_email_and_click_on_to_a_restore_bttn(self, browser):
        page = MainPage(browser)
        page.open()
        page.click_login_button()
        page = LoginPage(browser)
        page.click_on_restore_psswrd_link()
        page = PasswordRestorePage(browser)
        page.enter_email_and_confirm()
        url_4_assert = BASE_URL + PASSWORD_RESET_URL
        assert page.current_url() == url_4_assert, \
            f"Текущий URL {page.current_url()}"
        

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_click_on_show_password_highlighting_input_field(self, browser):
        page = MainPage(browser)
        page.open()
        page.click_login_button()
        page = LoginPage(browser)
        page.click_on_restore_psswrd_link()
        page = PasswordRestorePage(browser)
        page.enter_email_and_confirm()
        page.click_shows_password_icon()
        assert page.check_is_password_field_active(), \
            f'Поле не стало активным и подсвеченным'
