import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.constructor_page import ConstructorPage


@allure.story("Проверки «Лента заказов»")
class TestOrderFeed:


    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order_get_popup(self, browser):
        page = MainPage(browser)
        page.open()
        page.click_to_orders_feed_button()
        page = OrderFeedPage(browser)
        page.select_last_order()
        assert page.check_for_order_windows_visability(), \
            f'Окно с деталями не появилось'
        

    @allure.title("Заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_displayed_in_feed(self, browser, crt_order):
        orders_number = f"#0{crt_order}"
        page = MainPage(browser)
        page.open()
        page.click_to_orders_feed_button()
        page = OrderFeedPage(browser)
        assert page.find_order_in_order_list(orders_number), \
            f"Заказы не отображаются"


    @allure.title("При создании нового заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_orders_counter_change(self, browser, login_user):
        page = MainPage(browser)
        page.open()
        page.click_to_orders_feed_button()
        page = OrderFeedPage(browser)
        number_of_all_orders = page.get_number_of_total_orders()
        page.click_on_to_constructor_button()
        page = ConstructorPage(browser)
        page.create_an_order()
        page.click_to_orders_feed_button()
        page = OrderFeedPage(browser)
        number_of_all_orders_change = page.get_number_of_total_orders()
        assert number_of_all_orders_change > number_of_all_orders, \
            f"number_of_all_orders: {number_of_all_orders}, number_of_all_orders_change: {number_of_all_orders_change}"


    @allure.title("При создании нового заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_orders_counter_change(self, browser, login_user):
        page = MainPage(browser)
        page.open()
        page.click_to_orders_feed_button()
        page = OrderFeedPage(browser)
        number_of_all_orders = page.get_number_of_today_orders()
        page.click_on_to_constructor_button()
        page = ConstructorPage(browser)
        page.create_an_order()
        page.click_to_orders_feed_button()
        page = OrderFeedPage(browser)
        number_of_all_orders_change = page.get_number_of_today_orders()
        assert number_of_all_orders_change > number_of_all_orders, \
            f"number_of_all_orders: {number_of_all_orders}, number_of_all_orders_change: {number_of_all_orders_change}"


    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_new_order_shown_in_orders_in_work_list(self, browser, login_user):
        page = ConstructorPage(browser)
        order_number = page.create_an_order()
        page.click_to_orders_feed_button()
        page = OrderFeedPage(browser)
        order_in_work = page.get_number_in_work_list()
        assert order_number > order_in_work, \
            f"order_number: {order_number}, order_in_work: {order_in_work}"
        