from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.helpers.app import App


class CommonScreen(App):
    """
    common screen locators
    """
    def __init__(self):
        super().__init__()

    code_zero = (MobileBy.ID, "ru.mts.smartmed.dev:id/tbZero")