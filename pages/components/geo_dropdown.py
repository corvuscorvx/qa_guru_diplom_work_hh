import allure
from typing import Tuple

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from core.browser import Browser


class GeoDropdown:
    DROPDOWN = (By.CSS_SELECTOR, '[data-qa="drop-base"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, '[data-qa="drop-base"] [class*="header--"] > button')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-qa="geo-switcher-search"]')
    CLEAR_INPUT_BUTTON = (By.CSS_SELECTOR, '[data-qa="input-clearable-button"]')
    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, '[data-qa="drop-base"] [data-qa="cell"]')

    def __init__(self, browser: Browser):
        self.browser = browser

    @staticmethod
    def _get_city_locator(city_name: str) -> Tuple[str, str]:
        return By.XPATH, f'//*[@data-qa="drop-base"]//*[@data-qa="cell" and contains(., "{city_name}")]'

    def close_dropdown(self) -> None:
        self.browser.wait_for_element_visible(self.DROPDOWN)
        self.browser.click_element(self.CLOSE_BUTTON)

    def is_closed(self) -> bool:
        try:
            return self.browser.wait_for_element_invisible(self.DROPDOWN, timeout=3)
        except TimeoutException:
            return False

    def scroll_to_city(self, city_name: str) -> None:
        locator = self._get_city_locator(city_name)
        self.browser.scroll_to_element(locator)

    def search(self, text: str) -> None:
        self.browser.send_keys_to_element(self.SEARCH_INPUT, text)

    def clear_search_input(self) -> None:
        self.browser.click_element(self.CLEAR_INPUT_BUTTON)

    def get_text_in_input(self) -> str:
        return self.browser.get_attribute(self.SEARCH_INPUT, "value")

    def get_available_cities(self) -> list[str]:
        elements = self.browser.wait_for_elements_visible(self.SEARCH_RESULT_ITEMS)
        return [el.text.strip() for el in elements if el.text.strip()]

    def select_city(self, city_name: str) -> None:
        locator = self._get_city_locator(city_name)
        self.browser.click_element(locator)