from typing import Tuple, Optional
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec



class Browser:

    def __init__(self, driver: WebDriver, default_timeout: int = 10):
        self.driver = driver
        self.default_timeout = default_timeout
        self.wait = WebDriverWait(driver, default_timeout)

    def _wait(self, timeout: Optional[int] = None) -> WebDriverWait:
        return WebDriverWait(self.driver, timeout or self.default_timeout)

    def get_text(self, locator: Tuple[str, str]) -> str:
        element = self.wait_for_element_visible(locator)
        return element.text

    def get_attribute(self, locator: Tuple[str, str], attribute_name: str) -> str:
        element = self.wait_for_element_visible(locator)
        return element.get_attribute(attribute_name) or ""

    def get_current_url(self) -> str:
        return self.driver.current_url

    def wait_for_element_visible(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> WebElement:
        return self._wait(timeout).until(ec.visibility_of_element_located(locator))

    def wait_for_elements_visible(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> list[WebElement]:
        return self._wait(timeout).until(ec.visibility_of_all_elements_located(locator))

    def wait_for_element_clickable(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> WebElement:
        return self._wait(timeout).until(ec.element_to_be_clickable(locator))

    def wait_for_element_invisible(self, locator: Tuple[str, str], timeout: Optional[int] = None) -> bool:
        return bool(self._wait(timeout).until(ec.invisibility_of_element_located(locator)))

    def wait_for_url_in_new_tab(self, url_part: str) -> bool:
        self._wait().until(lambda driver: len(driver.window_handles) > 1)
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        return bool(self._wait().until(ec.url_contains(url_part)))

    def click_element(self, locator: Tuple[str, str]) -> None:
        element = self.wait_for_element_clickable(locator)
        element.click()

    def send_keys_to_element(self, locator: Tuple[str, str], text: str | int) -> None:
        text_to_send = str(text)
        element = self.wait_for_element_visible(locator)
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.BACKSPACE)
        element.send_keys(text_to_send)

    def scroll_to_element(self, locator: Tuple[str, str]) -> WebElement:
        element = self._wait().until(ec.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element