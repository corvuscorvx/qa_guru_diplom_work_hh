import allure
from selenium.webdriver.common.by import By

from core.browser import Browser


class Header:
    HELP_BUTTON = (By.CSS_SELECTOR, '[data-qa="help-button"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-qa="login mainmenu_loginButton"]')
    SERVICE_BUTTON = (By.CSS_SELECTOR, '[data-qa="allServices-button"]')
    GEO_CHANGE_BUTTON = (By.CSS_SELECTOR, '[data-qa="geoSwitcher-button"]')

    def __init__(self, browser: Browser):
        self.browser = browser

    def get_current_geo(self) -> str:
        return self.browser.get_text(self.GEO_CHANGE_BUTTON).strip()

    def press_the_geo_button(self) -> None:
        self.browser.click_element(self.GEO_CHANGE_BUTTON)

    def press_the_help_button(self) -> None:
        self.browser.click_element(self.HELP_BUTTON)

    def press_the_login_button(self) -> None:
        self.browser.click_element(self.LOGIN_BUTTON)

    def press_the_service_button(self) -> None:
        self.browser.click_element(self.SERVICE_BUTTON)





