from time import sleep

import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.handle_black import handle_black


class BasePage():
    _driver: WebDriver = None

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    @handle_black
    def find(self, locator):
        sleep(3)
        element = self._driver.find_element(*locator)
        WebDriverWait(self._driver, 2).until(expected_conditions.element_to_be_clickable(locator))
        return element

    def get_text(self, locator):
        text = self.find(locator).text
        return text

    def find_click(self, locator):
        return self.find(locator).click()

    def find_sendkeys(self, locator, text):
        return self.find(locator).send_keys(text)

    def roll_click(self, text):
        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector().'
                   'scrollable(true).instance(0)).'
                   'scrollIntoView(new UiSelector().'
                   f'text("{text}").instance(0));')
        return self.find_click(element)
