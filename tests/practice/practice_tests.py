from pages.practice.practice_page import PracticePage
from utilities.assertstatus import AssertStatus
from pages.home.navigation_page import NavigationPage
import unittest
import pytest
import allure

@pytest.mark.usefixtures("one_time_set_up", "set_up")
class PracticeTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUP(self, one_time_set_up):
        self.pc = PracticePage(self.driver)
        self.ts = AssertStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=1)
    @allure.feature("Radio buttons")
    @allure.story("Selecting radio buttons")
    def test_radioButtons(self):
        result1 = self.pc.switch_to_practice_page()
        self.ts.mark(result1, "test_switch_to_the_practice_page: ")
        result2 = self.pc.verify_title()
        self.ts.mark(result2, "Page title verification")
        result3 = self.pc.check_radio_buttons()
        self.ts.mark_final("test_radio_buttons: ", result3, "radio buttons verification")

    @pytest.mark.run(order=2)
    @allure.feature("Check boxes")
    @allure.story("Selecting/Unselecting checkboxes")
    def test_checkBoxes(self):
        result1 = self.pc.check_check_boxes()
        self.ts.mark(result1, "check_boxes checked")
        result2 = self.pc.check_unselect_elements()
        self.ts.mark_final("test_check_boxes", result2, "check_boxes verification")

    @pytest.mark.run(order=3)
    @allure.feature("Dropdown list")
    @allure.story("Selecting elements in the list")
    def test_dropDownList(self):
        result = self.pc.check_drop_down_list()
        self.ts.mark_final("test_dropDownList: ", result, "dropDownList verification")

    @pytest.mark.run(order=4)
    @allure.feature("Multiple value list")
    @allure.story("Selecting/Unselecting elements in the list")
    def test_multipleList(self):
        result1 = self.pc.check_multiple_value_list()
        self.ts.mark(result1, "elements selected")
        result2 = self.pc.check_unselect_elements()
        self.ts.mark_final("test_multipleList: ", result2, "multipleList verification")

    @pytest.mark.run(order=5)
    @allure.feature("Displayed/Hidden page elements")
    @allure.story("Checking the display of elements")
    def test_hiddenElements(self):
        result = self.pc.is_displayed()
        self.ts.mark_final("test_hiddenElements", result, "hiddenElements verification")

    @pytest.mark.run(order=6)
    @allure.feature("Enabled/Disabled page elements")
    @allure.story("Checking whether an element enabled/disabled")
    def test_disabledElements(self):
        result = self.pc.is_enabled()
        self.ts.mark_final("test_disableElements", result, "disableElements verification")

    @pytest.mark.run(order=7)
    @allure.feature("Alert window")
    @allure.story("Switching to the alert window")
    def test_switchToAlert(self):
        result = self.pc.check_switch_to_alert()
        self.ts.mark_final("test_switchToAlert", result, "switchToAlert verification")

    @pytest.mark.run(order=8)
    @allure.feature("Confirm window")
    @allure.story("Switching to the confirmation window")
    def test_switchToConfirm(self):
        result = self.pc.check_switch_to_confirm()
        self.ts.mark_final("test_switchToComfirm", result, "switchToComfirm verification")

    @pytest.mark.run(order=9)
    @allure.feature("Mouse hover element")
    @allure.story("Selecting items in the list")
    def test_mouseHoverOver(self):
        result = self.pc.check_mouse_hovering()
        self.ts.mark_final("test_mouseHoverOver", result, "mouseHoverOver verification")

    @pytest.mark.run(order=10)
    @allure.feature("Iframe of the page")
    @allure.story("Switching to the iframe of the page")
    def test_switchIframe(self):
        result = self.pc.check_switch_to_iframe()
        self.ts.mark_final("test_switchIframe", result, "switchIframe verification")

    @pytest.mark.run(order=11)
    @allure.feature("New page of the window")
    @allure.story("Switching to the new window")
    def test_switchToWindow(self):
        result1 = self.pc.switch_to_all_courses_page()
        self.ts.mark(result1, "switchWindow verification")
        result2 = self.pc.check_new_window_element()
        self.ts.mark_final("test_switch_to_allCoursesWindow", result2, "newWindow element verification")

    @pytest.mark.run(order=12)
    @allure.feature("Logout")
    @allure.story("User logout")
    def test_logout(self):
        result = self.pc.log_out()
        self.ts.mark_final("test_logout ", result, "logout verification after all tests ")
