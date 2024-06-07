import time
from base.basepage import BasePage
from utilities.assertstatus import AssertStatus
import utilities.custom_logger as cl
import logging
from pages.home.navigation_page import NavigationPage
import allure

class PracticePage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.st = AssertStatus(driver)

    _logout_button = "(//a[@href='/logout' and contains(text(), 'Logout')])"
    _element_practice_button = "(//a[normalize-space()='Element Practice'])"
    _radio_buttons_list = "(//input[contains(@type, 'radio') and contains(@name, 'cars')])"
    _check_boxes_list = "(//input[contains(@type, 'checkbox') and contains(@name, 'cars')])"
    _switch_new_window_button = "openwindow"
    _drop_down_list = "carselect"
    _multiple_select_list = "multiple-select-example"
    _show_element_button = "show-textbox"
    _hide_element_button = "hide-textbox"
    _displayed_text_field = "displayed-text"
    _disabled_button = "disabled-button"
    _enabled_button = "enabled-button"
    _enabled_disable_field = "enabled-example-input"
    _enter_your_name_button = "enter-name"
    _alert_button = "alertbtn"
    _confirm_button = "confirmbtn"
    _mouse_hover = "mousehover"
    _page_table = "(//table[@id='product'])"
    _iframe_locator = "courses-iframe"
    _new_window_logo = "img-fluid"
    _search_box = "(//*[@id='search' and @name='course'])"

    def check_radio_buttons(self):
        with allure.step("Check all radio buttons in the 'Radio Button Example' section"):
            self.element_list_presence_check(self._radio_buttons_list, "xpath")
            return self.select_elements(self._radio_buttons_list, locatorType="xpath")

    def check_check_boxes(self):
        with allure.step("Check all check boxes in the 'Checkbox Example' section"):
            self.element_list_presence_check(self._check_boxes_list, "xpath")
            return self.select_elements(self._check_boxes_list, locatorType="xpath")

    def check_unselect_elements(self):
        with allure.step("Unselect all the items in the section"):
            return self.un_select_elements(self._check_boxes_list, locatorType="xpath")

    def check_drop_down_list(self):
        with allure.step("Select all the items in the 'Select Class Example' section"):
            self.element_list_presence_check(self._drop_down_list, "id")
            return self.drop_down_select(self._drop_down_list, locatorType="id")

    def check_multiple_value_list(self):
        with allure.step("Select all items in the 'Multiple Select Example' section"):
            self.element_list_presence_check(self._multiple_select_list, "id")
            return self.drop_down_select(self._multiple_select_list, locatorType="id")

    def check_switch_to_alert(self):
        with allure.step("Enter 'Test' in the 'Switch to Alert Example' field"):
            self.send_keys("Test", self._enter_your_name_button, locatorType="name")
        with allure.step("Click on the 'Alert button' and click 'ok' in the alert window"):
            return self.switch_to_alert(self._alert_button, locatorType="id")

    def check_switch_to_confirm(self):
        with allure.step("Enter 'Test' in the 'Switch to Alert Example' field"):
            self.send_keys("Test", self._enter_your_name_button, locatorType="name")
        with allure.step("Click on the 'Confirm' button and click 'Cancel' in the confirm window"):
            return self.switch_to_confirm(self._confirm_button, locatorType="id")

    def check_mouse_hovering(self):
        with allure.step("Scroll down"):
            self.web_scroll(direction="little down")
        with allure.step("Hover the mouse over 'Mouse Hover' button and click on the 'Reload' item in the list"):
            time.sleep(3)
            return self.hover_mouse_over(self._mouse_hover, locatorType="id")

    def check_switch_to_iframe(self):
        with allure.step("Scroll down"):
            self.web_scroll(direction="down")
            self.switch_to_frame(id=self._iframe_locator)
        with allure.step("Enter 'Python' in the 'Search Course' field and click on the 'magnifier' icon"):
            self.send_keys("Python", self._search_box, locatorType="xpath")
            time.sleep(1)
            self.switch_to_default_content()
        with allure.step("Scroll up"):
            self.web_scroll(direction="up")
        with allure.step("Enter 'Test' in the 'enter your name' field"):
            return self.send_keys("Test", self._enter_your_name_button, locatorType="name")

    def verify_title(self):
        with allure.step("Check that the page title is 'Practice page'"):
            return self.verify_page_title("Practice page")


    def is_displayed(self):
        with allure.step("Click on the 'Hide' button in the 'Element Displayed Example' section"):
            self.element_click(self._hide_element_button, locatorType="id")
        with allure.step("Check that the 'Hide/Show Example' field has disappeared"):
            self.is_element_displayed(self._displayed_text_field, locatorType="id")
        with allure.step("Click on the 'Show' button in the 'Element Displayed Example' section"):
            self.element_click(self._show_element_button, locatorType="id")
        with allure.step("Check that the 'Hide/Show Example' field has appeared"):
            self.is_element_displayed(self._displayed_text_field, locatorType="id")
        with allure.step("Enter 'Test' in the 'Hide/Show Example' field"):
            return self.send_keys("Test", self._displayed_text_field, locatorType="id")

    def is_enabled(self):
        with allure.step("Click on the 'Disable' button in the 'Enabled/Disabled Example' section"):
            self.element_click(self._disabled_button, locatorType="id")
        with allure.step("Check that the 'Enabled/Disabled' field isn't activ"):
            self.is_element_enabled(self._enabled_disable_field, locatorType="id", info="'enabled_disable_field'")
        with allure.step("Click on the 'Enable' button in the 'Enabled/Disabled Example' section"):
            self.element_click(self._enabled_button, "id")
        with allure.step("Check that the 'Enabled/Disabled' field is activ"):
            self.is_element_enabled(self._enabled_disable_field, locatorType="id", info="'enabled_disable_field'")
        with allure.step("Enter 'Test' in the 'Enabled/Disabled' field"):
            return self.send_keys("Test", self._enabled_disable_field, locatorType="id")

    def check_new_window_element(self):
        with allure.step("Check that 'Let's Kode it' logo is displayed in the new window"):
            return self.is_element_present(self._new_window_logo, "class")

    def switch_to_practice_page(self):
        with allure.step("Click on the 'Practice' tab at the top of the window"):
            self.nav.navigate_to_practice_tab()
        with allure.step("Click on the 'Element Practice' item"):
            return self.switch_to_tab(self._element_practice_button, locatorType="xpath")

    def switch_to_all_courses_page(self):
        with allure.step("Click on the 'Open window' button in the 'Switch Window Example' section"):
            return self.switch_to_window(self._switch_new_window_button, "id")

    def log_out(self):
        with allure.step("Click on the 'User settings' icon at the top of the window"):
            self.nav.navigate_to_user_settings()
        with allure.step("Click on the 'log out' item"):
            logout_link = self.wait_for_element(self._logout_button,
                                                locatorType="xpath", pollFrequency=1)
            return self.element_click(element=logout_link)

