import time

from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    browser = open_basket_page(browser)
    browser.add_product_to_basket()
    browser.solve_quiz_and_get_code()


def open_basket_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    browser = ProductPage(browser, link)
    browser.open()
    return browser
