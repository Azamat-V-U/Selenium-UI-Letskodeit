from base.basepage import BasePage
import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
import time
import allure

class LoginPage(BasePage):

    log = cl.custom_logger((logging.DEBUG))

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    _signin_button = "(//a[@class='dynamic-link' and text()='Sign In'])"
    _email_field = "(//input[@type='email' and @placeholder='Email Address'])"
    _password_field = "(//input[@type='password'])"
    _login_button = "(//button[@id='login'])"
    _logout_button = "(//a[@href='/logout' and contains(text(), 'Logout')])"
    _invalid_login_message = "(//span[contains(text(), 'Incorrect login details. Please try again.')])"
    _login_verification_icon = "(//button[@id='dropdownMenu1'])"

    def click_sign_in_button(self):
        self.element_click(self._signin_button, locatorType="xpath")

    def enter_email(self, email):
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        with allure.step("Click on the 'sign in' button"):
            self.click_sign_in_button()
        with allure.step("Enter email"):
            self.enter_email(email)
        with allure.step("Enter password"):
            self.enter_password(password)
        with allure.step("Click on the 'log in' button"):
            self.click_login_button()
        time.sleep(3)

    def verify_title(self):
        with allure.step("Verify page title"):
            return self.verify_page_title("Login")

    def verify_login_successful(self):
        with allure.step("Verify login successful"):
            return self.is_element_present(self._login_verification_icon, locatorType="xpath")

    def verify_login_failed(self):
        with allure.step("Verify login failed"):
            return self.is_element_present(self._invalid_login_message, locatorType="xpath")


    def log_out(self):
        with allure.step("Hover over user settings"):
            self.nav.navigate_to_user_settings()
        logout_link = self.wait_for_element(self._logout_button,
                                            locatorType="xpath", pollFrequency=1)
        with allure.step("Click on the 'log out' button"):
            self.element_click(element=logout_link)





