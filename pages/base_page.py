import allure

from core.browser import Browser
from pages.components.header import Header
from pages.components.geo_dropdown import GeoDropdown


class BasePage:
    def __init__(self, browser: Browser):
        self.browser = browser
        self.header = Header(browser)
        self.geo_dropdown = GeoDropdown(browser)

    @allure.step("Получить текущий URL страницы")
    def get_current_url(self) -> str:
        return self.browser.get_current_url()