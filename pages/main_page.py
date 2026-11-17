#TODO: разобраться с поп-апами про куки и гео при хаоде на сайт (смотри ОС по дз про триколор)
import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    PHONE_NUMBER_INPUT = (By.CSS_SELECTOR, '[data-qa="account-signup-email"]')

    def input_phone_number(self, phone_number: str) -> None:
        self.browser.send_keys_to_element(self.PHONE_NUMBER_INPUT, phone_number)