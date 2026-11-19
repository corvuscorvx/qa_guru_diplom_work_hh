import allure
from typing import Tuple

from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from core.browser import Browser


class GeoDropdown:
    DROPDOWN = (By.CSS_SELECTOR, '[data-qa="drop-base"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, '[data-qa="drop-base"] [class*="header--"] > button')
    SEARCH_INPUT = (By.CSS_SELECTOR, '[data-qa="geo-switcher-search"]')
    CLEAR_INPUT_BUTTON = (By.CSS_SELECTOR, '[data-qa="input-clearable-button"]')
    EMPTY_CITY_MESSAGE = (By.CSS_SELECTOR, '[data-qa="drop-base"] [class*="magritte-text_typography-title-5-semibold"]')
    SEARCH_RESULT_ITEMS = (By.CSS_SELECTOR, '[data-qa="drop-base"] [data-qa="cell"]')


    def __init__(self, browser: Browser):
        self.browser = browser

    @staticmethod
    def _get_city_locator(city_name: str) -> Tuple[str, str]:
        return By.XPATH, f'//*[@data-qa="drop-base"]//*[@data-qa="cell" and contains(., "{city_name}")]'

    @allure.step('Закрыть выпадающий список')
    def close_dropdown(self) -> None:
        self.browser.wait_for_element_visible(self.DROPDOWN)
        self.browser.click_element(self.CLOSE_BUTTON)

    @allure.step('Проверить, что выпадающий список закрыт')
    def is_closed(self) -> bool:
        try:
            return self.browser.wait_for_element_invisible(self.DROPDOWN, timeout=3)
        except TimeoutException:
            return False

    @allure.step('Скролить список до искомого города')
    def scroll_to_city(self, city_name: str) -> None:
        locator = self._get_city_locator(city_name)
        self.browser.scroll_to_element(locator)

    @allure.step('Поиск в выпадающем списке')
    def search(self, text: str) -> None:
        self.browser.send_keys_to_element(self.SEARCH_INPUT, text)

    @allure.step('Очистить поле поиска')
    def clear_search_input(self) -> None:
        self.browser.click_element(self.CLEAR_INPUT_BUTTON)

    @allure.step('Дождаться результатов поиска, содержащих "{expected_substring}"')
    def wait_for_search_results(self, expected_substring: str, timeout: int = 5) -> list[str]:
        def _results_match(_):
            cities = self.get_available_cities()
            return bool(cities) and all(
                expected_substring.lower() in city.lower() for city in cities
            )

        self.browser.wait_until(_results_match, timeout=timeout)
        return self.get_available_cities()

    @allure.step('Получить список доступных городов')
    def get_available_cities(self) -> list[str]:
        try:
            elements = self.browser.wait_for_elements_visible(self.SEARCH_RESULT_ITEMS, timeout=2)
            return [el.text.strip() for el in elements if el.text.strip()]
        except (StaleElementReferenceException, TimeoutException):
            return []

    @allure.step('Выбрать город "{city_name}" из списка')
    def select_city(self, city_name: str) -> None:
        locator = self._get_city_locator(city_name)
        self.browser.click_element(locator)

    @allure.step('Получить текст сообщения об отсутствии результатов')
    def get_empty_search_message(self) -> str:
        return self.browser.get_text(self.EMPTY_CITY_MESSAGE).strip()

    @allure.step('Получить текст из поля ввода')
    def get_text_in_input(self) -> str:
        return self.browser.get_attribute(self.SEARCH_INPUT, "value")