from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select


class BasePage:
    """
    This class contains all of the common functions used for the pages.
    """
    url = None

    def __init__(self, context):
        self.driver = context.driver
        self.context = context

    def visit(self):
        self.driver.get(self.context.config.userdata.get('ui_base_url') + self.url)

    def find_element(self, by, locator):
        try:
            return self.driver.find_element(by, locator)
        except NoSuchElementException:
            return None

    def find_element_from_element(self, element, by, locator):
        try:
            return element.find_element(by, locator)
        except NoSuchElementException:
            return None

    def select(self, by, locator):
        try:
            return Select(self.driver.find_element(by, locator))
        except NoSuchElementException:
            return None
