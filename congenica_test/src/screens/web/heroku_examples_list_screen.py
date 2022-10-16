from selenium.webdriver.common.by import By

from congenica_test.src.helpers.app import App


class HerokuExamplesListScreen(App):
    """
    Locators containing links to heroku examples pages
    """
    def get_example_link_by_text(self, text):
        return self.wait_until_clickable((By.XPATH, f"//a[contains(text(), '{text}')]"))