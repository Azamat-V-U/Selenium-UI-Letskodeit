from base.basepage import BasePage
import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
import time
import allure


class LoginPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    _signin_button = "(//a[@class='dynamic-link' and text()='Sign In'])"
    _email_field = "(//input[@type='email' and @placeholder='Email Address'])"
    _password_field = "(//input[@type='password'])"
    _login_button = "(//button[@id='login'])"
    _logout_button = "(//a[@href='/logout' and contains(text(), 'Logout')])"
    _invalid_login_message = "(//span[contains(text(), 'Incorrect login details')])"
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
        with allure.step("Verify the page title"):
            return self.verify_page_title("Login")

    def verify_login_successful(self):
        with allure.step("Verify that login is successful"):
            return self.is_element_present(self._login_verification_icon, locatorType="xpath")

    def verify_login_failed(self):
        with allure.step("Verify that the login is failed"):
            return self.is_element_present(self._invalid_login_message, locatorType="xpath")

    def log_out(self):
        with allure.step("Click on the 'User settings' icon at the top of the window"):
            self.nav.navigate_to_user_settings()
            logout_link = self.wait_for_element(self._logout_button,
                                                locatorType="xpath", pollFrequency=1)
            self.log.info("Log out button is ready")
        with allure.step("Click on the 'log out' item"):
            self.element_click(element=logout_link)
