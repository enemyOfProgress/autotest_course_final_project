from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    page = open_browser(browser)
    page.go_to_login_page()


def test_guest_should_see_login_link(browser):
    page = open_browser(browser)
    page.should_be_login_link()


def open_browser(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser, link)
    page.open()
    return page
