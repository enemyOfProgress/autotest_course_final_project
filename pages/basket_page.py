from .base_page import BasePage


class BasketPage(BasePage):
    def is_basket_empty(self, by, locator):
        empty_message = self.browser.find_element(by, locator)
        assert empty_message, "The basket isn't empty"
