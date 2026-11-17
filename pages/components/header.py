import allure
from selenium.webdriver.common.by import By

from core.browser import Browser


class Header:
    HELP_BUTTON = (By.CSS_SELECTOR, '[data-qa="help-button"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-qa="login mainmenu_loginButton"]')
    GEO_CHANGE_BUTTON = (By.CSS_SELECTOR, '[data-qa="geoSwitcher-button"]')

    def __init__(self, browser: Browser):
        self.browser = browser

    def press_the_geo_button(self) -> None:
        self.browser.click_element(self.GEO_CHANGE_BUTTON)

    def press_the_help_button(self) -> None:
        self.browser.click_element(self.HELP_BUTTON)

    def press_the_login_button(self) -> None:
        self.browser.click_element(self.LOGIN_BUTTON)



