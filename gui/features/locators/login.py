from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = By.ID, 'username'
    PASSWORD = By.ID, 'password'
    LOGIN_BTN = By.CSS_SELECTOR, '[name="login"]'
    ERROR_MESSAGE = By.CSS_SELECTOR, '.woocommerce-error li'
