from selenium.webdriver.common.by import By


class ProductDetailsLocators:
    PRODUCT_COLOR = By.ID, 'pa_color'
    PRODUCT_LOGO = By.ID, 'logo'
    PRODUCT_QUANTITY = By.CSS_SELECTOR, '[name="quantity"]'
    PRODUCT_PRICE = By.CSS_SELECTOR, '.single_variation_wrap .price'
    ADD_TO_CART_BTN = By.CSS_SELECTOR, '.single_add_to_cart_button'
