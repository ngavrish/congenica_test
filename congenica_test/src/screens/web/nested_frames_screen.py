from selenium.webdriver.common.by import By

from congenica_test.src.helpers.app import App


class NestedFramesScreen(App):
    """
    locators for nested frames screen
    """
    frame_left_index = 0
    frame_middle_index = 1
    frame_right_index = 2
    frame_bottom = (By.XPATH, "//frame[@src='frame-bottom']")
    frame_top_index = 0
    frame_bottom_index = 1
    div_content = (By.ID, "content")
