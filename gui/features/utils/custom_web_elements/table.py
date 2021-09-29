from selenium.common.exceptions import UnexpectedTagNameException
from selenium.webdriver.common.by import By


class Table:
    def __init__(self, webelement):
        """
        Constructor. A check is made that the given element is, indeed, a TABLE tag. If it is not,
        then an UnexpectedTagNameException is thrown.

        :Args:
         - webelement - element TABLE element to wrap

        Example:
            Table(driver.find_element_by_tag_name("table")).exist_header("text")
        """

        if webelement.tag_name != "table":
            raise UnexpectedTagNameException("Table only works on <table> elements, not on <%s>" % webelement.tag_name)
        self._el = webelement

    def body_rows(self):
        """
        This method gets all rows in the table under the tbody section, ignoring the rows in the theader section
        """
        return self._el.find_elements(By.CSS_SELECTOR, "tbody tr")

    @staticmethod
    def get_cell_from_row(row):
        return row.find_elements(By.CSS_SELECTOR, 'td')
