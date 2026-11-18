import allure
from selenium.webdriver.common.by import By

from core.browser import Browser


class GeoDropdown:
    DROPDOWN = (By.CSS_SELECTOR, '[data-qa="drop-base"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, '[data-qa="drop-base"] [class*="header--"] > button')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-qa="geo-switcher-search"]')
    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, '[data-qa="drop-base"] [data-qa="cell"]')

    def __init__(self, browser: Browser):
        self.browser = browser

    def close_dropdown(self) -> None:
        self.browser.wait_for_element_visible(self.DROPDOWN)
        self.browser.click_element(self.CLOSE_BUTTON)
        # self.browser.wait_for_element_invisible(self.DROPDOWN)

    def search(self, text: str) -> None:
        self.browser.send_keys_to_element(self.SEARCH_INPUT, text)

    def get_result_search(self) -> str:
        return self.browser.get_text(self.SEARCH_RESULT_ITEMS)

    def select_city(self, city_name: str) -> None:
        cities = self.browser.wait_for_elements_visible(self.SEARCH_RESULT_ITEMS)
        for city in cities:
            if city_name in city.text:
                city.click()
                return
        raise ValueError(f"Не удалось выбрать город '{city_name}': элемент не найден в списке")