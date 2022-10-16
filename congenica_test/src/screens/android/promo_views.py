from appium.webdriver.common.mobileby import MobileBy

from congenica_test.src.helpers.app import App


class PromoScreen(App):
    """
    Promo screen locators
    """

    class November25Years():
        image = (MobileBy.ID, 'ru.mts.smartmed.dev:id/itemWhatToNewImage')
        close_view = (MobileBy.ID, 'ru.mts.smartmed.dev:id/whatToNewCloseBtn')


