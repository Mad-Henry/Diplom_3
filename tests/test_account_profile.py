import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from URLs import USER_ACCOUNT_PROFILE_URL, USER_ACCOUNT_HISTORY_URL, LOGIN_PAGE_URL


@allure.story("Проверки 'Личный кабинет'")
class TestAccountProfile:


    @allure.title("Переход в Личный кабинет по клику на «Личный кабинет»")
    def test_go_to_profile_from_main_page(self, browser, login_user):
        page = MainPage(browser)
        page.move_in_profile_after_auth()
        assert page.current_url() == USER_ACCOUNT_PROFILE_URL, \
            f'URL is: {page.current_url()}'


    @allure.title("Переход в раздел «История заказов» из профиля")
    def test_go_to_order_history_from_profile(self, browser, login_user):
        page = MainPage(browser)
        page.move_in_profile_after_auth()
        page = AccountPage(browser)
        page.click_on_order_history_menu()
        assert page.current_url() == USER_ACCOUNT_HISTORY_URL, \
            f'URL is: {page.current_url()}'


    @allure.title("Выход из аккаунта через личный кабинет")
    def test_logout_from_profile_page(self, browser, login_user):
        page = MainPage(browser)
        page.move_in_profile_after_auth()
        page = AccountPage(browser)
        page.click_logout_from_account()
        assert page.current_url() == LOGIN_PAGE_URL, \
            f'URL is: {page.current_url()}'
        