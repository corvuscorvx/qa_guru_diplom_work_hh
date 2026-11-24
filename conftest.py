import os
from urllib.parse import urlparse

import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from utils import attach
from core.browser import Browser
from pages.main_page import MainPage

load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        default="chrome",
        help="Browser to use"
    )
    parser.addoption(
        "--browser_version",
        default="157.0",
        choices=("148.0", "157.0", "158.0"),
        help="Browser version to use"
    )
    parser.addoption(
        "--window_size",
        default="1920*1080",
        help="Window size"
    )
    parser.addoption(
        "--base_url",
        default=os.getenv("BASE_URL"),
        help="Base URL of the site under test"
    )


@pytest.fixture(scope="function")
def base_url(request):
    return request.config.getoption("--base_url")


@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    browser_version = request.config.getoption("--browser_version")
    window_size = request.config.getoption("--window_size")
    url = request.config.getoption("--base_url")

    options = ChromeOptions()
    width, height = window_size.split("*")
    options.add_argument(f"--window-size={width},{height}")

    selenoid_capabilities = {
        "browserName": browser,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "screenResolution": f"{width}x{height}x24"
        }
    }
    options.capabilities.update(selenoid_capabilities)

    selenoid_url = os.getenv("SELENOID_URL")
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_password = os.getenv("SELENOID_PASSWORD")

    command_executor = f"https://{selenoid_login}:{selenoid_password}@{selenoid_url}/wd/hub"

    driver = webdriver.Remote(
        command_executor=command_executor,
        options=options
    )

    driver.set_window_size(int(width), int(height))
    # driver.implicitly_wait(5)

    if url:
        clean_url = url.rstrip("/")
        host = urlparse(clean_url).netloc

        driver.get(f"{clean_url}/favicon.ico")
        driver.add_cookie({
            "name": "region_clarified",
            "value": host,
            "domain": ".hh.ru",
            "path": "/"
        })
        driver.add_cookie({
            "name": "cookie_policy_agreement",
            "value": "true",
            "domain": ".hh.ru",
            "path": "/"
        })

    yield driver

    attach.add_screenshot(driver)
    attach.add_page_source(driver)
    attach.add_console_logs(driver)
    attach.add_video(driver)

    driver.quit()


@pytest.fixture(scope="function")
def browser(driver):
    return Browser(driver)


@pytest.fixture(scope="function")
def main_page(browser, base_url):
    browser.driver.get(f"{base_url}")
    return MainPage(browser)


@pytest.fixture(scope="function")
def opened_geo_dropdown(main_page):
    main_page.header.click_geo_button()
    return main_page.geo_dropdown


@pytest.fixture(scope="function")
def opened_chat_widget(main_page):
    main_page.header.click_help_button()
    main_page.help_modal.click_support_button()
    main_page.chat_widget.switch_to_frame()
    return main_page.chat_widget
