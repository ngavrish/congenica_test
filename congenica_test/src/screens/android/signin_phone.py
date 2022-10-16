from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.helpers.app import App


class SignInPhoneScreen(App):
    """
    Send phone number
    """

    phone_input = (MobileBy.ID, "ru.mts.smartmed.dev:id/txtPhoneNumber")
    next_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/button_text")
    LOGIN_PATIENT = {"phone": "8771234567", "password": "00000000"}

    def fill_phone_number(self):
        self.set_field(self.phone_input, self.LOGIN_PATIENT['phone'])
        self.wait_until_clickable(self.next_button).click()
