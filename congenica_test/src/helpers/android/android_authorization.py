from congenica_test.src.data.patient import Patient
from congenica_test.src.screens.android.allow_location import AllowLocationScreen
from congenica_test.src.screens.android.city_selection import CitySelectionScreen
from congenica_test.src.screens.android.login import LoginScreen
from congenica_test.src.screens.android.send_sms_code import SendSmsCodeScreen
from congenica_test.src.screens.android.signin_button import SignInButtonScreen
from congenica_test.src.screens.android.signin_password import SignInPasswordScreen
from congenica_test.src.screens.android.signin_phone import SignInPhoneScreen
from congenica_test.src.screens.android.welcome import WelcomeTutorialScreen
from congenica_test.src.utils import get_activation_code


def android_authorization(driver):
    welcome_screen = WelcomeTutorialScreen(driver)
    allow_location_screen = AllowLocationScreen(driver)
    allow_location_screen.skip_location()
    city_selection_screen = CitySelectionScreen(driver)
    city_selection_screen.select_city()
    welcome_screen.skip_tutorial_button()
    login_screen = LoginScreen(driver)
    sign_in_button_screen = SignInButtonScreen(driver)
    sign_in_button_screen.click_to_login_btn()
    sign_in_phone_screen = SignInPhoneScreen(driver)
    sign_in_phone_screen.fill_phone_number()
    sign_in_password_screen = SignInPasswordScreen(driver)
    sign_in_password_screen.fill_password_field()
    code = get_activation_code(Patient.PHONE)
    send_sms_code_screen = SendSmsCodeScreen(driver)
    send_sms_code_screen.enter_sms_code(code)
    login_screen.enter_login_pin()
    login_screen.dont_allow_notification()
    driver.terminate_app("ru.medsi.smartmed.dev")
    driver.launch_app()
    login_screen.enter_pin()
