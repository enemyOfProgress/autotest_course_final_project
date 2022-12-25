import time

from .pages.main_page import MainPage
from .pages.locators import BasketPageLocators
from .pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    browser = open_browser(browser, MainPage)
    login_page = browser.go_to_login_page()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    browser = open_browser(browser, MainPage)
    browser.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    browser = open_browser(browser, BasketPage)
    browser.go_to_the_basket()
    browser.is_basket_empty(*BasketPageLocators.EMPTY_BASKET)


def open_browser(browser, page):
    link = "http://selenium1py.pythonanywhere.com/"
    browser = page(browser, link)
    browser.open()
    return browser
