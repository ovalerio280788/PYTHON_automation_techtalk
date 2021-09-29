from selenium.webdriver.common.by import By


class CartLocators:
    PRODUCTS_TABLE = By.CSS_SELECTOR, 'table.shop_table.cart'
    CART_TOTALS_TABLE = By.CSS_SELECTOR, '.cart_totals table'
    ITEM_QUANTITY = By.CSS_SELECTOR, '[id^="quantity"]'
