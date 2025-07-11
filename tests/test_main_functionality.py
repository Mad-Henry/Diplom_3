import allure
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from URLs import BASE_URL, ORDER_FEED_URL


@allure.story("Проверка основного функционала")
class TestMainFeatures:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_on_constructor_button(self, browser):
        page = MainPage(browser)
        page.open("login")
        page.click_to_constructor_button()
        assert page.current_url() == BASE_URL, \
            f'{page.current_url()}'


    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_on_order_list_button(self, browser):
        page = MainPage(browser)
        page.open()
        page.click_to_orders_feed_button
        assert page.current_url() == ORDER_FEED_URL, \
            f'{page.current_url()}'
        

    @allure.title("Если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_click_on_ingredient_shows_details(self, browser):
        page = ConstructorPage(browser)
        page.open()
        page.set_bun()
        assert page.check_for_details_window(), \
            f'Окно не появилоась'


    @allure.title("Всплывающее окно закрывается кликом по крестику")
    def test_close_ingredient_details_window_by_click(self, browser):
        page = ConstructorPage(browser)
        page.open()
        page.set_bun()
        page.check_for_details_window()
        assert page.close_details_window(), \
            f'Окно не закрылось'
        

    @allure.title("При добавлении ингредиента в заказ счётчик этого ингридиента увеличивается")
    def test_ingredient_counter(self, browser):
        page = ConstructorPage(browser)
        page.open()
        page.add_bun_to_order()
        counter = page.ingredients_counter()
        assert counter == "2", \
            f'counter: {counter}'


    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_auth_user_can_create_an_order(self, browser, login_user):
        page = ConstructorPage(browser)
        number_of_order = page.create_an_order()
        assert number_of_order, \
            f'number_of_order: {number_of_order}'
        