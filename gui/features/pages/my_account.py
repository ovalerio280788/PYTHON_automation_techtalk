from gui.features.locators.login import LoginLocators
from gui.features.locators.my_account import MyAccountLocators
from gui.features.pages.base_page import BasePage
from gui.features.utils.singleton import singleton


@singleton
class MyAccountPage(BasePage):
    url = 'my-account/'

    @property
    def my_account_content(self):
        return self.find_element(*MyAccountLocators.MY_ACCOUNT_CONTENT)
