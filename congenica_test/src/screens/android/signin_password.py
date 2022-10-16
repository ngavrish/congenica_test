from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.helpers.app import App


class SignInPasswordScreen(App):
    """
    Signin password screen
    """

    password_input = (MobileBy.ID, "ru.mts.smartmed.dev:id/txtPassword")
    signin_button = (MobileBy.ID, "ru.mts.smartmed.dev:id/button_text")
    new_password_input = (MobileBy.ID, "ru.mts.smartmed.dev:id/password_new_input_text")
    LOGIN_PATIENT = {"phone": "8888887766", "password": "00000000"}

    def fill_password_field(self):
        self.set_field(self.password_input, self.LOGIN_PATIENT['password'])
        self.wait_until_clickable(self.signin_button).click()
