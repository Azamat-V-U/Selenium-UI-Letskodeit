from pages.home.login_page import LoginPage
from utilities.assertstatus import AssertStatus
from pages.home.navigation_page import NavigationPage
import unittest
import pytest

@pytest.mark.usefixtures("one_time_set_up", "set_up")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUP(self, one_time_set_up):
        self.lp = LoginPage(self.driver)
        self.ts = AssertStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        result = self.lp.verifyLoginSuccessful()
        self.ts.mark_final("test_validLogin", result, "ValidLogin verification")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logOut()
        self.lp.login("test@email.com", "afgtue")
        result1 = self.lp.verify_title()
        self.ts.mark(result1, "Title verification")
        result2 = self.lp.verifyLoginFailed()
        self.ts.mark_final("test_invalidLogin", result2, "InvalidLogin verification")


