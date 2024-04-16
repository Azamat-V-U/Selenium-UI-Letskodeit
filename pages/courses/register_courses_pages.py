import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _search_box = "(//input[@id='search' and @placeholder='Search Course'])"
    _search_button = "(//button[@class='find-course search-course'])"
    _all_courses = "(//a[@class='dynamic-link' and text()='ALL COURSES'])"
    _course = "(//div[@id='course-list']//h4[@class='dynamic-heading' and contains (text(),'{0}')])"
    _enroll_button = "(//button[@class='dynamic-button btn btn-default btn-lg btn-enroll' and text()='Enroll in Course'])"
    _cc_num = "(//input[@aria-label='Credit or debit card number'])"
    _cc_exp = "(//input[@name='exp-date'])"
    _cc_cvc = "(//input[@name='cvc'])"
    _submit_enroll = "(//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button'])"
    _enrol_error_message = "(//span[normalize-space()='Your card number is incorrect.'])[1]"

    def click_all_courses_tab(self):
        self.element_click(self._all_courses, locatorType="xpath")

    def enter_course_name(self, name):
        self.send_keys(name, self._search_box)
        return self.element_click(self._search_button, locatorType="xpath")

    def select_course_to_enroll(self, fullCourseName):
        return self.element_click(locator=self._course.format(fullCourseName), locatorType="xpath")

    def click_enroll_to_course_button(self):
        self.element_click(self._enroll_button)

    def enter_card_num(self, num):
        # time.sleep(3)
        self.switch_to_frame_by_index(self._cc_num, locatorType="xpath")
        self.send_keys_when_ready(num, locator=self._cc_num, locatorType="xpath")
        self.switch_to_default_content()

    def enter_card_exp(self, exp):
        # time.sleep(3)
        self.switch_to_frame_by_index(self._cc_exp, locatorType="xpath")
        self.send_keys_when_ready(exp, locator=self._cc_exp, locatorType="xpath")
        self.switch_to_default_content()

    def enter_card_cvc(self, cvc):
        # time.sleep(3)
        self.switch_to_frame_by_index(self._cc_cvc, locatorType="xpath")
        self.send_keys_when_ready(cvc, locator=self._cc_cvc, locatorType="xpath")
        self.switch_to_default_content()

    def enter_credit_card_information(self, num, exp, cvc):
        self.enter_card_num(num)
        self.enter_card_exp(exp)
        self.enter_card_cvc(cvc)

    def click_enroll_submit_button(self):
        return self.element_click(self._submit_enroll, locatorType="xpath")

    def enroll_course(self, num="", exp="", cvc=""):
        self.web_scroll(direction="little down")
        self.click_enroll_to_course_button()
        self.web_scroll(direction="down")
        self.enter_credit_card_information(num, exp, cvc)
        time.sleep(3)
        return self.click_enroll_submit_button()

    def verify_enroll_failed(self):
        # time.sleep(3)
        result = self.is_element_displayed(locator=self._enrol_error_message,
                                           locatorType="xpath")
        return result



