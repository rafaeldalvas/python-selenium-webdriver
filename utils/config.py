from selenium import webdriver
from abc import ABC

class PageElement(ABC):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver

    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)


