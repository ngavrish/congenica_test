from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.helpers.app import App


class ChatScreen(App):

    chat_message_field = (MobileBy.ACCESSIBILITY_ID, "Введите сообщение")
    go_back = (MobileBy.ACCESSIBILITY_ID, "Back")
