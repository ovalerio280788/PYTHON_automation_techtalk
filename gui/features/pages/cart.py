from gui.features.locators.cart import CartLocators
from gui.features.pages.base_page import BasePage
from gui.features.utils.singleton import singleton


@singleton
class CartPage(BasePage):
    url = 'cart/'

    @property
    def products_table(self):
        return self.find_element(*CartLocators.PRODUCTS_TABLE)

    @property
    def cart_totals_table(self):
        return self.find_element(*CartLocators.CART_TOTALS_TABLE)

    def quantity_from_table_cell(self, cell):
        return self.find_element_from_element(cell, *CartLocators.ITEM_QUANTITY)
