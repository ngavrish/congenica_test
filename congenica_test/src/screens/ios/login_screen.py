from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.data.patient import Patient
from congenica_test.src.helpers.app import App
from congenica_test.src.screens.ios.signin_password import SignInPasswordScreen
from congenica_test.src.screens.ios.signin_phone import SignInPhoneScreen


class LoginScreen(App):
    """
    login screen locators
    """

    inputField = (MobileBy.ACCESSIBILITY_ID, "input-email")
    passwordField = (MobileBy.ACCESSIBILITY_ID, "input-password")
    loginButton = (MobileBy.XPATH, "//XCUIElementTypeStaticText[@name='LOGIN']")
    ENTER_BTN = (MobileBy.ACCESSIBILITY_ID, "Войти")
    ENTER_SMS_FIELD = (MobileBy.IOS_PREDICATE, "type == 'XCUIElementTypeTextField'")
    SMS_SCREEN_HEADER = (MobileBy.ACCESSIBILITY_ID, "Введите код из смс")
    ZERO_BTN = (MobileBy.ACCESSIBILITY_ID, "0")
    ENTER_PIN = (MobileBy.ACCESSIBILITY_ID, "Создайте код доступа")
    ENTER_PIN_AGAIN = (MobileBy.ACCESSIBILITY_ID, "Повторите код доступа")
    ENTER_PIN_SECOND = (MobileBy.ACCESSIBILITY_ID, "Введите код доступа")
    NOT_ALLOW = (MobileBy.ACCESSIBILITY_ID, "Don’t Allow")
    ALLOW = (MobileBy.ACCESSIBILITY_ID, "Allow")
    INFO_MSG = (MobileBy.ACCESSIBILITY_ID, "Notifications may include alerts, sounds and icon badges. These can be "
                                           "configured in Settings.")

    def click_to_login_btn(self):
        if self.find_element(self.ENTER_BTN):
            self.click_to_element(self.ENTER_BTN)

    def fill_phone_number(self):
        self.set_field(SignInPhoneScreen.phone_input, Patient.PHONE)
        while self.wait_for_text_in_locator(SignInPhoneScreen.phone_input).text != Patient.PHONE:
            self.click_to_element(SignInPhoneScreen.clear_button)
            self.set_field(SignInPhoneScreen.phone_input, Patient.PHONE)
        self.tap_by_coordinates(x=163, y=319)
        self.click_to_element(SignInPhoneScreen.next_button)

    def fill_password_field(self):
        self.set_field(SignInPasswordScreen.password_input, Patient.PASSWORD)
        self.click_to_element(SignInPasswordScreen.hidden_password)
        self.wait_until_visible_locator(SignInPasswordScreen.password_inside)
        while self.wait_until_visible_locator(SignInPasswordScreen.password_inside).text != Patient.PASSWORD:
            action = ActionChains(self.driver)
            action.send_keys_to_element(SignInPasswordScreen.password_inside,
                                        Keys.CONTROL + 'a', Keys.BACKSPACE)
            action.release()
            self.set_field(SignInPasswordScreen.password_inside, Patient.PASSWORD)
        self.tap_by_coordinates(x=163, y=319)
        self.click_to_element(SignInPasswordScreen.signin_button)

    def enter_sms_code(self, code):
        self.set_field(self.ENTER_SMS_FIELD, code)

    def enter_login_pin(self):
        self.wait_for_text_in_locator(self.ENTER_PIN)
        for i in range(0, 4):
            self.click_to_element(self.ZERO_BTN)
        self.wait_for_text_in_locator(self.ENTER_PIN_AGAIN)
        for i in range(0, 4):
            self.click_to_element(self.ZERO_BTN)

    def enter_pin(self):
        if self.wait_until_not_invisible(self.SMS_SCREEN_HEADER):
            for i in range(0, 4):
                self.click_to_element(self.ZERO_BTN)

    def dont_allow_notification(self):
        button = self.wait_until_clickable(self.NOT_ALLOW)
        button.click()

