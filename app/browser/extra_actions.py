"""Module for providing extra actions for Selenium browsers."""

from typing import Tuple

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_element(browser: WebDriver, locator: Tuple[str, str], timeout: int = 10) -> WebElement:
    """
    Waits for an element to be visible and returns it.

    Args:
        browser: the browser that will be used to wait for the element
        locator: the locator of the element that will be waited for
                 (e.g. (By.ID, "my-id"))
        timeout: the max amount of time to wait for the element to be visible

    Returns:
        The element that was waited for
    """
    wait = WebDriverWait(browser, timeout)
    element = wait.until(EC.visibility_of_element_located(locator))  # type: ignore # noqa
    return element  # type: ignore
