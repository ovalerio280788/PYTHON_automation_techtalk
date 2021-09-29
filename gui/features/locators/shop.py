from selenium.webdriver.common.by import By


class ShopLocators:
    PRODUCTS = By.CSS_SELECTOR, '.products li'
    PRODUCT_TITTLE = '//h5[@class="woocommerce-loop-product__title"][text()="{}"]/ancestor::li/a'
