from base.basepage import BasePage
import utilities.custom_logger as cl
from pages.home.navigation_page import NavigationPage
import logging
import time

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

    def click_sign_in_button(self):
        self.element_click(self._signin_button, locatorType="xpath")

    def enter_email(self, email):
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.element_click(self._login_button, locatorType="xpath")

    def login(self, email="", password=""):
        self.click_sign_in_button()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(3)

    def verify_title(self):
        return self.verify_page_title("Login")


    def verifyLoginSuccessful(self):
        return self.is_element_present("(//button[@id='dropdownMenu1'])",
                                       locatorType="xpath")


    def verifyLoginFailed(self):
        return self.is_element_present("(//span[contains(text(), 'Incorrect login details. Please try again.')])",
                                       locatorType="xpath")



    def logOut(self):
        self.nav.navigate_to_user_settings()
        logout_link = self.wait_for_element(self._logout_button,
                                            locatorType="xpath", pollFrequency=1)
        self.element_click(element=logout_link)





