import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from core.browser import Browser


class HelpModal:
    MODAL = (By.CSS_SELECTOR, '[data-qa="modal-overlay"] [role="dialog"]')
    CLOSE_BUTTON = (By.CSS_SELECTOR, '[data-qa="modal-overlay"] button[aria-label="Закрыть окно помощи"]')
    SUPPORT_CHAT_BUTTON = (By.CSS_SELECTOR, '[data-qa="support-chat-button"]')

    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step('Нажать кнопку "Закрыть окно"')
    def click_close_button(self) -> None:
        self.browser.click_element(self.CLOSE_BUTTON)

    @allure.step('Проверить, что окно "Нужна помощь?" закрыто')
    def is_closed(self) -> bool:
        try:
            return self.browser.wait_for_element_invisible(self.MODAL, timeout=3)
        except TimeoutException:
            return False

    @allure.step('Нажать кнопку "Спросить в чате"')
    def click_support_button(self) -> None:
        self.browser.click_element(self.SUPPORT_CHAT_BUTTON)