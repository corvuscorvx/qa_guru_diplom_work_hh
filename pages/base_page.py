import allure

from core.browser import Browser
from pages.components.header import Header


class BasePage:
    def __init__(self, browser: Browser):
        self.browser = browser
        self.header = Header(browser)

