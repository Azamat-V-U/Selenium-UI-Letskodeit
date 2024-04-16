import utilities.custom_logger as cl
from base.basepage import BasePage
import logging

class NavigationPage(BasePage):

    log = cl.custom_logger((logging.DEBUG))

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _my_courses_icon = "All courses"
    _user_settings_icon = "(//div[@class='dropdown']/button[@id='dropdownMenu1'])"
    _practice_tab_icon = "(//a[@type='button' and contains(text(), 'PRACTICE')])"

    def navigate_to_all_courses(self):
        self.element_click(locator=self._my_courses_icon, locatorType="link")

    def navigate_to_user_settings(self):
        user_settings_element = self.wait_for_element(locator=self._user_settings_icon,
                                                      locatorType="xpath", pollFrequency=1)
        self.element_click(element=user_settings_element)

    def navigate_to_practice_tab(self):
        practice_tab = self.wait_for_element(locator=self._practice_tab_icon,
                                             locatorType="xpath", pollFrequency=1)
        self.element_click(element=practice_tab)

