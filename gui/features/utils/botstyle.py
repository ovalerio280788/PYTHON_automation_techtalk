from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def write_in_field(web_element, text, clear=True):
    """
    This method types the provided text in a textfield.
    params:
    web_element = web element
    text = the string you need to type in the field
    """
    if clear:
        web_element.clear()
    web_element.send_keys(text)


def is_button_disabled(web_element):
    """
    This method verifies if a button is disable
    params: a button web element
    return: True is the button is disabled
    """
    return True if "disabled" in web_element.get_attribute("class") else False


def wait_for_element_to_have_class(driver, element, class_name, timeout_in_seconds=5):
    """
    This method waits for an element to have a given class
    params:
        - driver: the instance of the webdriver
        - element: the element to check if has a given class or not
        - class_name: the expected class name that the element should have
        - timeout_in_seconds: the time to wait for the element to have the class.
    """
    try:
        wait = WebDriverWait(driver, timeout_in_seconds)
        return wait.until(element_has_css_class(element, class_name, True))
    except:
        return None


def scroll_to_element(driver, element):
    driver.execute_script("arguments[0].scrollIntoView();", element)


def scroll_to_offset(driver, element, x, y):
    driver.execute_script(f"arguments[0].scrollTo({x},{y});", element)


def mouse_over(driver, element, highlight=True):
    """
    This method do a mouse hover over a given element
    Params:
        - driver: the webdriver instance
        - Element: element to do the mouse hover action
    """
    ActionChains(driver).move_to_element(element).perform()
    highlight_element(driver, element) if highlight else None
    return element


def highlight_element(driver, element):
    """
    This method highlight a given element
    Params:
        - driver: the webdriver instance
        - Element: element to mark with yellow background and border color red
    """
    driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');", element)


def actions_press_key(driver, key):
    """
    This method perform a press key based on a given key as parameter
    @param driver: the webdriver instance
    @param key: The key object to use, use the Keys object that selenium provodes, i.e, Keys.ESCAPE
    @return: NA
    """
    ActionChains(driver).send_keys(key).perform()


def mouse_over_with_offset(driver, element, x, y):
    """
    This method do a mouse hover over a given element using x and y offset
    Params:
        - driver: the webdriver instance
        - Element: element to do the mouse hover action and the offset
    """
    ActionChains(driver).move_to_element_with_offset(element, x, y).perform()
    return element


def wait_for_element_to_have_css_property(driver, element, css_property, property_value, timeout_in_seconds=5):
    """
    This method waits for an element to have a given class
    params:
        - driver: the instance of the webdriver
        - element: the element to check if has a given class or not
        - class_name: the expected class name that the element should have
        - timeout_in_seconds: the time to wait for the element to have the class.
    """
    try:
        wait = WebDriverWait(driver, timeout_in_seconds)
        return wait.until(element_has_css_property(element, css_property, property_value, True))
    except:
        return None


def wait_for_element_to_not_have_css_property(driver, element, css_property, property_value, timeout_in_seconds=10):
    """
    This method waits for an element to NOT have a given class
    params:
        - driver: the instance of the webdriver
        - element: the element to check if has a given class or not
        - class_name: the expected class name that the element should NOT have
        - timeout_in_seconds: the time to wait for the element to NOT have the class.
    """
    try:
        wait = WebDriverWait(driver, timeout_in_seconds)
        return wait.until(element_has_css_property(element, css_property, property_value, False))
    except:
        return None


def click_on_button_js(driver, element):
    driver.execute_script(f"arguments[0].click();", element)


def wait_for_element_to_be_visible(driver, element, wait_for=3):
    try:
        return WebDriverWait(driver, wait_for).until(EC.visibility_of(element))
    except Exception as e:
        return None


def wait_for_element_to_be_enable(driver, element, wait_for=3):
    try:
        return WebDriverWait(driver, wait_for).until(is_button_disabled(element) is False)
    except Exception as e:
        return None


class element_has_css_class(object):
    """An expectation for checking that an element has a particular css class.
    element - the element to check
    returns the WebElement once it has the particular css class
    """

    def __init__(self, element, css_class, should_have_class):
        self.element = element
        self.css_class = css_class
        self.should_have_class = should_have_class

    def __call__(self, driver):
        if self.should_have_class:
            return True if self.css_class in self.element.get_attribute("class") else False
        else:
            return True if self.css_class not in self.element.get_attribute("class") else False


class element_has_css_property(object):
    """An expectation for checking that an element has a particular css property.
    element - the element to check
    returns True if it has the particular css property
    """

    def __init__(self, element, css_property, property_value, should_have_class):
        self.element = element
        self.css_property = css_property
        self.property_value = property_value
        self.should_have_class = should_have_class

    def __call__(self, driver):
        if self.should_have_class:
            return True if self.property_value in self.element.value_of_css_property(self.css_property) else False
        else:
            return True if self.css_property not in self.element.value_of_css_property("class") else False
