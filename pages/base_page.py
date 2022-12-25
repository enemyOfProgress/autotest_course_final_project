import math
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def get_current_url(self):
        return self.browser.current_url

    def switch_to_current_page(self, link):
        return self.browser.switch_to.window(link)

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link isn't presented"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_the_basket(self):
        open_basket = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        open_basket.click()

    def is_element_present(self, by, locator):
        try:
            self.browser.find_element(by, locator)
        except NoSuchElementException:
            return False

        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_presented(self, by, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout)\
                .until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, by, locator, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException)\
                .until_not(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return False

        return True

