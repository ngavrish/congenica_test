import time
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from congenica_test.settings import WAIT_TIMEOUT_SEC


class App:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, WAIT_TIMEOUT_SEC)

    def highlight(self, element, effect_time=2, color="blue", border=5):
        """Highlights (blinks) a Selenium Webdriver element"""
        driver = element._parent

        def apply_style(s):
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                                  element, s)

        original_style = element.get_attribute('style')
        apply_style("border: {0}px solid {1};".format(border, color))
        time.sleep(effect_time)
        apply_style(original_style)

    def switch_to_frame(self, locator):
        self.wait.until(EC.frame_to_be_available_and_switch_to_it(locator))

    def wait_until_elements_are_present(self, locator):
        """
        :param locator: element locator
        :return: element present on screen
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_until_present(self, locator):
        """
        :param locator: element locator
        :return: element present on screen
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_until_visible_locator(self, locator):
        """
        :param locator: element locator
        :return: element visible on screen
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_not_invisible(self, locator):
        """
        :param locator: element locator
        :return: True if element is not visible
        """
        self.wait.until(EC.invisibility_of_element(locator))
        return True

    def wait_until_clickable(self, locator):
        """
        :param locator: element locator
        :return: web element that can be clickable
        """
        return self.wait.until(EC.element_to_be_clickable(locator))

    def tap_by_coordinates(self, x, y):
        """
        :param x: x coordinate
        :param y: y coordinate
        :return: void
        """
        actions = TouchAction(self.driver)
        actions.tap(x=x, y=y).perform()
