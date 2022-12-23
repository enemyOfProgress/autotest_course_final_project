from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):
    def waiter(self):
        wait = WebDriverWait(self.browser, 5)
        return wait

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def is_message_visible(self, by, locators):
        text_from_message = self.waiter().until(
            EC.visibility_of_element_located((by, locators)))
        return text_from_message.text

    def compare_the_product(self, product_from_message):
        product_from_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_PRODUCT)
        assert product_from_message in product_from_cart.text, "It's not the same product"

    def compare_the_amount(self, message_with_amount):
        product_amount = self.browser.find_element(*ProductPageLocators.PRICE_FROM_PRODUCT)
        assert product_amount.text in message_with_amount, "The amount is different"
