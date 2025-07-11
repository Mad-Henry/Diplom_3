import pytest
from selenium import webdriver
from helpers import HelpersMethods as HM
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


@pytest.fixture(params=["Chrome", "Firefox"])
def browser(request):
    if request.param == "Chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    yield browser
    browser.quit()


@pytest.fixture
def create_user():
    data = HM.generate_creds()
    response, _ = HM.create_user(data)
    yield response, data
    HM.delete_user({"Authorization": response["accessToken"]})


@pytest.fixture
def login_user(browser, create_user):
    _, data = create_user
    user_email = data["email"]
    user_password = data["password"]

    page = MainPage(browser)
    page.open()
    page.click_profile_button()
    page = LoginPage(browser)
    page.login_in_to_a_profile(email=user_email, password=user_password)


@pytest.fixture
def create_order(browser, login_user):
    page = ConstructorPage(browser)
    return page.create_an_order()
