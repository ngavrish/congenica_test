from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.helpers.app import App


class CitySelectionScreen(App):
    """
    city selection screen 
    """

    spb_city = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Санкт-Петербург')]")
    moscow_city = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Москва')]")
    continue_button = (MobileBy.XPATH, "//android.widget.TextView[contains(@text, 'Далее')]")

    def select_city(self):
        self.wait_until_clickable(self.moscow_city).click()
        self.wait_until_clickable(self.continue_button).click()
