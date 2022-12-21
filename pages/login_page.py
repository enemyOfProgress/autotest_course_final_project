from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        link = self.browser.current_url
        login = "login"
        assert login in link, "The 'login' isn't present in link"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "The login form isn't present"

    def should_be_register_form(self):
        registration_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert registration_form, "The registration form isn't present"
