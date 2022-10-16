import pytest
from selenium.webdriver.common.by import By

from congenica_test.settings import HEROKUAPP_URL
from congenica_test.src.helpers.app import App
from congenica_test.src.screens.web.challenging_dom_screen import ChallengingDomScreen
from congenica_test.src.screens.web.dynamically_loaded_elements_screen import \
    DyncamicallyLoadedElementsScreen
from congenica_test.src.screens.web.heroku_examples_list_screen import HerokuExamplesListScreen
from congenica_test.src.screens.web.nested_frames_screen import NestedFramesScreen


class TestCongenicoCodingChallenge:

    def test_task_one(self, driver):
        driver.get(HEROKUAPP_URL)
        heroku_examples_list = HerokuExamplesListScreen(driver)
        nested_frames_screen = NestedFramesScreen(driver)
        heroku_examples_list.get_example_link_by_text("Frames").click()
        heroku_examples_list.get_example_link_by_text("Nested Frames").click()

        nested_frames_screen.switch_to_frame(nested_frames_screen.frame_top_index)
        nested_frames_screen.switch_to_frame(nested_frames_screen.frame_middle_index)
        middle_text = nested_frames_screen.wait_until_present((By.XPATH, "//body")).text
        driver.switch_to.default_content()

        nested_frames_screen.switch_to_frame(nested_frames_screen.frame_top_index)
        nested_frames_screen.switch_to_frame(nested_frames_screen.frame_left_index)
        left_text = nested_frames_screen.wait_until_present((By.XPATH, "//body")).text
        driver.switch_to.default_content()

        nested_frames_screen.switch_to_frame(nested_frames_screen.frame_top_index)
        nested_frames_screen.switch_to_frame(nested_frames_screen.frame_right_index)
        right_text = nested_frames_screen.wait_until_present((By.XPATH, "//body")).text
        driver.switch_to.default_content()

        nested_frames_screen.switch_to_frame(nested_frames_screen.frame_bottom_index)
        bottom_text = nested_frames_screen.wait_until_present((By.XPATH, "//body")).text
        driver.switch_to.default_content()

        print(f"\n{middle_text}\n{bottom_text}\n{left_text}\n{right_text}\n")
        assert True

    def test_task_two(self, driver):
        driver.get(f"{HEROKUAPP_URL}/dynamic_loading/1")
        dynamically_loaded_elements_screen = DyncamicallyLoadedElementsScreen(driver)
        dynamically_loaded_elements_screen.wait_until_clickable(
            dynamically_loaded_elements_screen.button_start).click()
        dynamically_loaded_elements_screen.wait_until_visible_locator(dynamically_loaded_elements_screen.div_loading)
        dynamically_loaded_elements_screen.wait_until_not_invisible(dynamically_loaded_elements_screen.div_loading)
        print("\n" + dynamically_loaded_elements_screen.wait_until_visible_locator(
            dynamically_loaded_elements_screen.h4_finish).text)

        assert True

    def test_task_three(self, driver):
        driver.get(f"{HEROKUAPP_URL}/challenging_dom")
        challenging_dom_screen = ChallengingDomScreen(driver)
        challenging_dom_screen \
            .highlight(challenging_dom_screen
                       .wait_fo_cell_by_row_and_column(3,
                                                       challenging_dom_screen.get_column_index_by_column_header(
                                                           "Diceret")))
        challenging_dom_screen.highlight(
            challenging_dom_screen.wait_for_clickable_link_by_cell_text_and_link_text('Apeirian7', 'delete'))
        challenging_dom_screen.highlight(
            challenging_dom_screen.wait_for_clickable_link_by_cell_text_and_link_text('Apeirian2', 'edit'))
        challenging_dom_screen \
            .highlight(challenging_dom_screen
                       .wait_fo_cell_by_row_and_column(7,
                                                       challenging_dom_screen.get_column_index_by_column_cell(
                                                           "Definiebas")))
        challenging_dom_screen \
            .highlight(challenging_dom_screen
                       .wait_fo_cell_by_row_and_column(7,
                                                       challenging_dom_screen.get_column_index_by_column_cell(
                                                           "Iuvaret")))
        challenging_dom_screen.wait_until_clickable(challenging_dom_screen.button_qux).click()
