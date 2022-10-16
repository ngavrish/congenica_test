from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.helpers.app import App


class SignInButtonScreen(App):
    """
    Signing button screen
    """

    button = (MobileBy.ID, "ru.mts.smartmed.dev:id/button_text")

    def click_to_login_btn(self):
        self.wait_until_clickable(self.button).click()