import pytest

from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators


@pytest.mark.parametrize('offer_number', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser, offer_number):
    browser = open_basket_page(browser, offer_number)
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


def open_basket_page(browser, offer_number):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{offer_number}"
    browser = ProductPage(browser, link)
    browser.open()
    return browser
