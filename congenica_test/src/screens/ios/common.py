from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.helpers.app import App


class CommonScreen(App):
    """
    common screen locators
    """

    def __init__(self, driver):
        super().__init__(driver)

    code_zero = (MobileBy.ACCESSIBILITY_ID, '0')