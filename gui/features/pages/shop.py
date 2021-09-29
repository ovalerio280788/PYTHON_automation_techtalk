from selenium.common.exceptions import NoSuchElementException

from gui.features.locators.shop import ShopLocators
from gui.features.pages.base_page import BasePage
from gui.features.utils.singleton import singleton


@singleton
class ShopPage(BasePage):
    url = '/'

    def product_with_name(self, product_name):
        try:
            return self.driver.find_element_by_xpath(ShopLocators.PRODUCT_TITTLE.format(product_name))
        except NoSuchElementException:
            return None
