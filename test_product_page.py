import pytest

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators, BasketPageLocators
from .pages.basket_page import BasketPage


# @pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser):
    browser = open_product_page(browser, ProductPage)
    browser.add_product_to_basket()
    browser.solve_quiz_and_get_code()

    # Check that the message with product name is visible, after user add product in cart
    product = browser.is_message_visible(*ProductPageLocators.MESSAGE_PRODUCT_NAME_IN_CART)
    # Compare product from cart and product from product page
    browser.compare_the_product(product)

    # Check that the message with amount is visible, after user add product in cart
    amount = browser.is_message_visible(*ProductPageLocators.MESSAGE_WITH_AMOUNT)
    # Compare amount in cart and product amount
    browser.compare_the_amount(amount)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    browser = open_product_page(browser, ProductPage)
    browser.add_product_to_basket()
    is_message_visible = browser.is_not_element_presented(*ProductPageLocators.MESSAGE_PRODUCT_NAME_IN_CART)
    print(is_message_visible)
    assert is_message_visible, "The message should be, but test is ok"


def test_guest_cant_see_success_message(browser):
    browser = open_product_page(browser, ProductPage)
    is_message_visible = browser.is_not_element_presented(*ProductPageLocators.MESSAGE_PRODUCT_NAME_IN_CART)
    print(is_message_visible)
    assert is_message_visible, "The message shouldn't be"


def test_message_disappeared_after_adding_product_to_basket(browser):
    browser = open_product_page(browser, ProductPage)
    browser.add_product_to_basket()
    message_is_disappear = browser.is_disappeared(*ProductPageLocators.MESSAGE_PRODUCT_NAME_IN_CART)
    assert message_is_disappear, "The message is still here"


def test_guest_should_see_login_link_on_product_page(browser):
    browser = open_product_page(browser, ProductPage)
    browser.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    browser = open_product_page(browser, ProductPage)
    browser.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    browser = open_product_page(browser, BasketPage)
    browser.go_to_the_basket()
    browser.is_basket_empty(*BasketPageLocators.EMPTY_BASKET)


def open_product_page(browser, page):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    browser = page(browser, link)
    browser.open()
    return browser
