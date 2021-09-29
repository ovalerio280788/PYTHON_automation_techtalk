from gui.features.locators.login import LoginLocators
from gui.features.pages.base_page import BasePage
from gui.features.utils.singleton import singleton


@singleton
class LoginPage(BasePage):
    url = 'my-account/'

    @property
    def username(self):
        return self.find_element(*LoginLocators.USERNAME)

    @property
    def password(self):
        return self.find_element(*LoginLocators.PASSWORD)

    @property
    def login_btn(self):
        return self.driver.find_element(*LoginLocators.LOGIN_BTN)

    @property
    def error_message(self):
        return self.driver.find_element(*LoginLocators.ERROR_MESSAGE)
