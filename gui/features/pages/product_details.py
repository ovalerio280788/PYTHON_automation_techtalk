from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select

from gui.features.locators.product_details import ProductDetailsLocators
from gui.features.locators.shop import ShopLocators
from gui.features.pages.base_page import BasePage
from gui.features.utils.singleton import singleton


@singleton
class ProductDetailsPage(BasePage):

    @property
    def product_color(self):
        return self.select(*ProductDetailsLocators.PRODUCT_COLOR)

    @property
    def product_logo(self):
        return self.select(*ProductDetailsLocators.PRODUCT_LOGO)

    @property
    def product_quantity(self):
        return self.find_element(*ProductDetailsLocators.PRODUCT_QUANTITY)

    @property
    def product_price(self):
        return self.find_element(*ProductDetailsLocators.PRODUCT_PRICE)

    @property
    def add_to_cart_btn(self):
        return self.find_element(*ProductDetailsLocators.ADD_TO_CART_BTN)
