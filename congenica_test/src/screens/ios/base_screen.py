from congenica_test.src.helpers.app import App


class BaseScreen(App):
    """
    common screen locators
    """

    def __init__(self, driver):
        super().__init__(driver)