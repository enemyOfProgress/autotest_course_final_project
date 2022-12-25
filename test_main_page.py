import time

from .pages.main_page import MainPage
from .pages.locators import BasketPageLocators
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    page = open_browser(browser)
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = open_browser(browser)
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    browser = open_browser(browser)
    browser.go_to_the_basket()
    new_link = browser.get_current_url()
    page = BasketPage(browser, new_link)
    page.browser.is_basket_empty()


def open_browser(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    return page
