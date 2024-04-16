import time
from base.basepage import BasePage
from utilities.assertstatus import AssertStatus
import utilities.custom_logger as cl
import logging
from pages.home.navigation_page import NavigationPage


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
    # _check_box_bmw = "bmwcheck"
    # _check_box_benz = "benzcheck"
    # _check_box_honda = "hondacheck"
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
        self.element_list_presence_check(self._radio_buttons_list, "xpath")
        return self.select_elements(self._radio_buttons_list, locatorType="xpath")

    def check_check_boxes(self):
        self.element_list_presence_check(self._check_boxes_list, "xpath")
        return self.select_elements(self._check_boxes_list, locatorType="xpath")

    def check_unselect_elements(self):
        return self.un_select_elements(self._check_boxes_list, locatorType="xpath")

    def check_drop_down_list(self):
        self.element_list_presence_check(self._drop_down_list, "id")
        return self.drop_down_select(self._drop_down_list, locatorType="id")

    def check_multiple_value_list(self):
        self.element_list_presence_check(self._multiple_select_list, "id")
        return self.drop_down_select(self._multiple_select_list, locatorType="id")

    def check_switch_to_alert(self):
        self.send_keys("Test", self._enter_your_name_button, locatorType="name")
        return self.switch_to_alert(self._alert_button, locatorType="id")

    def check_switch_to_confirm(self):
        self.send_keys("Test", self._enter_your_name_button, locatorType="name")
        return self.switch_to_confirm(self._confirm_button, locatorType="id")

    def check_mouse_hovering(self):
        self.web_scroll(direction="little down")
        time.sleep(3)
        return self.hover_mouse_over(self._mouse_hover, locatorType="id")

    def check_switch_to_iframe(self):
        self.web_scroll(direction="down")
        self.switch_to_frame(id=self._iframe_locator)
        self.send_keys("Python", self._search_box, locatorType="xpath")
        time.sleep(1)
        self.switch_to_default_content()
        self.web_scroll(direction="up")
        return self.send_keys("Test", self._enter_your_name_button, locatorType="name")

    def verify_title(self):
        return self.verify_page_title("Practice page")

    # def is_selected(self):
    #     return self.is_element_selected(self._check_box_honda, locatorType="id")

    def is_displayed(self):
        self.element_click(self._hide_element_button, locatorType="id")
        self.is_element_displayed(self._displayed_text_field, locatorType="id")
        self.element_click(self._show_element_button, locatorType="id")
        self.send_keys("Test", self._displayed_text_field, locatorType="id")
        return self.is_element_displayed(self._displayed_text_field, locatorType="id")

    def is_enabled(self):
        self.element_click(self._disabled_button, locatorType="id")
        self.is_element_enabled(self._enabled_disable_field, locatorType="id", info="'enabled_disable_field'")
        self.element_click(self._enabled_button, "id")
        self.is_element_enabled(self._enabled_disable_field, locatorType="id", info="'enabled_disable_field'")
        return self.send_keys("Test", self._enabled_disable_field, locatorType="id")

    def check_new_window_element(self):
        return self.is_element_present(self._new_window_logo, "class")

    def switch_to_practice_page(self):
        self.nav.navigate_to_practice_tab()
        return self.switch_to_tab(self._element_practice_button, locatorType="xpath")

    def switch_to_all_courses_page(self):
        return self.switch_to_window(self._switch_new_window_button, "id")

    def log_out(self):
        self.nav.navigate_to_user_settings()
        logout_link = self.wait_for_element(self._logout_button,
                                            locatorType="xpath", pollFrequency=1)
        return self.element_click(element=logout_link)

