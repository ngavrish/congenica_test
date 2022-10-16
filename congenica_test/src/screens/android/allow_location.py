from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.helpers.app import App
from congenica_test.src.utils import is_out_of_timer


class AllowLocationScreen(App):
    """
    location screen locators
    """

    skipLocationButton = (MobileBy.ID, "ru.mts.smartmed.dev:id/permission_location_skip")
    permitLocationButton = (MobileBy.ID, "ru.mts.smartmed.dev:id/permission_location_request_button")

    @is_out_of_timer
    def skip_location(self):
        btn = self.wait_until_visible_locator(self.skipLocationButton)
        btn.click()
