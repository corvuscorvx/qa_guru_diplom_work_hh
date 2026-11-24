import allure
from selenium.common import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from core.browser import Browser


class ChatWidget:
    CHAT_TITLE = (By.CSS_SELECTOR, '[data-qa="participant-info-title"]')
    CHATS_LIST = (By.XPATH, '//*[@data-qa="chatik-layout"]//*[normalize-space()="Чаты"]')
    CHAT_IFRAME = (By.CSS_SELECTOR, 'iframe[data-qa="chatik-root"], [data-qa="chatik-root"] iframe')
    CHAT_WIDGET = (By.CSS_SELECTOR, '[data-qa="chatik-root"]')
    MENU_BUTTON = (By.CSS_SELECTOR, '[data-qa="chatik-chat-menu"]')
    BACK_BUTTON = (By.CSS_SELECTOR, '[data-qa="chatik-back-to-chats-button"]')
    BOTTOM_SHEET = (By.CSS_SELECTOR, '[data-qa="bottom-sheet-content"]')
    MESSAGE_TEXT = (By.CSS_SELECTOR, '[data-qa="chat-bubble-text"]')
    RATE_CHAT_BUTTON = (By.CSS_SELECTOR, '[data-qa="chatik-chat-rate-chat"]')
    CLOSE_CHAT_BUTTON = (By.CSS_SELECTOR, '[data-qa="chatik-close-chatik"]')
    TOGGLE_NOTIFICATIONS_BUTTON = (By.CSS_SELECTOR, '[data-qa*="chatik-chat-toggle-notifications"]')

    def __init__(self, browser: Browser):
        self.browser = browser

    @allure.step('Проверить, что виджет отображается')
    def is_opened(self) -> bool:
        try:
            return bool(self.browser.wait_for_element_visible(self.CHAT_WIDGET, timeout=5))
        except TimeoutException:
            return False

    @allure.step('Переключиться в окно чата')
    def switch_to_frame(self) -> None:
        self.browser.switch_to_frame(self.CHAT_IFRAME, timeout=10)

    @allure.step('Получить название открытого чата')
    def get_chat_title(self) -> str:
        return self.browser.get_text(self.CHAT_TITLE, timeout=10).strip()

    @allure.step('Нажать кнопку "Закрыть чат"')
    def close(self) -> None:
        self.browser.switch_to_default_content()
        self.browser.click_element(self.CLOSE_CHAT_BUTTON)

    @allure.step('Проверить, что виджет закрыт')
    def is_closed(self) -> bool:
        try:
            return self.browser.wait_for_element_invisible(self.CHAT_WIDGET, timeout=3)
        except TimeoutException:
            return False

    @allure.step('Открыть меню чата')
    def open_menu(self) -> None:
        self.browser.click_element(self.MENU_BUTTON)

    @allure.step('Проверить, что ботомшит отображается')
    def is_opened_bottom_sheet(self) -> bool:
        try:
            return bool(self.browser.wait_for_element_visible(self.BOTTOM_SHEET, timeout=5))
        except TimeoutException:
            return False

    @allure.step('Проверить, что ботомшит не отображается')
    def is_closed_bottom_sheet(self) -> bool:
        try:
            return self.browser.wait_for_element_invisible(self.BOTTOM_SHEET, timeout=5)
        except TimeoutException:
            return False

    @allure.step('Получить текст кнопки управления уведомлениями')
    def get_notifications_button_text(self) -> str:
        return self.browser.get_text(self.TOGGLE_NOTIFICATIONS_BUTTON).replace("\xa0", " ").strip()

    @allure.step('Переключить состояние уведомлений в чате')
    def switch_toggle_notifications(self) -> None:
        self.browser.click_element(self.TOGGLE_NOTIFICATIONS_BUTTON)

    @allure.step('Нажать кнопку "Оценить диалог с поддержкой"')
    def click_rate_chat(self) -> None:
        self.browser.click_element(self.RATE_CHAT_BUTTON)

    @allure.step('Получить текст последнего сообщения в чате')
    def get_last_message_text(self) -> str:
        elements = self.browser.wait_for_elements_visible(self.MESSAGE_TEXT)
        return elements[-1].text.replace("\xa0", " ").strip()

    @allure.step('Дождаться появления сообщения с текстом "{expected_text}"')
    def wait_for_last_message(self, expected_text: str, timeout: int = 15) -> str:
        def _last_message_matches(_):
            try:
                elements = self.browser.wait_for_elements_visible(self.MESSAGE_TEXT, timeout=2)
                if not elements:
                    return False
                last_text = elements[-1].text.replace("\xa0", " ").strip()
                return expected_text in last_text
            except (StaleElementReferenceException, TimeoutException):
                return False

        self.browser.wait_until(_last_message_matches, timeout=timeout)
        return self.get_last_message_text()

    @allure.step('Нажать кнопку "Назад" к списку всех чатов')
    def click_back_button(self) -> None:
        self.browser.click_element(self.BACK_BUTTON)

    @allure.step('Проверить, что отображается экран "Чаты"')
    def is_chats_list_displayed(self) -> bool:
        try:
            return bool(self.browser.wait_for_element_visible(self.CHATS_LIST, timeout=5))
        except TimeoutException:
            return False
