from selenium.webdriver.common.by import By

from congenica_test import logger
from congenica_test.src.helpers.app import App


class ChallengingDomScreen(App):
    """
    locators for challenging DOM screen
    """
    thead_cells = (By.XPATH, "//th")
    td_cells = (By.XPATH, "//td")
    button_qux = (By.XPATH, "//a[contains(text(), 'qux')]")

    def get_column_index_by_column_header(self, header):
        """
        :param header: text containg header index for witch we are looking for
        :return: index of column containing given header
        """
        i = 1
        for head_cell in self.wait_until_elements_are_present(self.thead_cells):
            if head_cell.text == header:
                return i
            i += 1
        return None

    def get_column_index_by_column_cell(self, cell_text):
        """
        :param header: text containg header index for witch we are looking for
        :return: index of column containing given header
        """
        i = 1
        for cell in self.wait_until_elements_are_present(self.td_cells):
            if cell_text.lower() in cell.text.lower():
                return i
            i += 1
        return None

    def wait_fo_cell_by_row_and_column(self, row_inex, column_index):
        """
        :param row_inex: index of row
        :param column_index: index of column
        :return: webelement
        """
        return self.wait_until_present((By.XPATH, f"//tr[{row_inex}]/td[{column_index}]"))

    def wait_for_clickable_link_by_cell_text_and_link_text(self, cell_text, link_text):
        return self.wait_until_clickable((By.XPATH, f"//td[text()='{cell_text}']/..//a[text()='{link_text}']"))
