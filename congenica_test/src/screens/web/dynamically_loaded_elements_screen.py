from selenium.webdriver.common.by import By

from congenica_test.src.helpers.app import App


class DyncamicallyLoadedElementsScreen(App):
    """
    locators for dynamically loaded elements screen
    """
    button_start = (By.XPATH, "//button[text()='Start']")
    div_loading = (By.ID, "loading")
    h4_finish = (By.XPATH, "//div[@id='finish']/h4")
