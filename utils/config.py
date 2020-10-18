from abc import ABC
from selenium.common.exceptions import NoAlertPresentException


class PageElement(ABC):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver

    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)

