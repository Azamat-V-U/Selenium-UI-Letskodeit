from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.assertstatus import AssertStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import get_csv_data
from pages.home.navigation_page import NavigationPage
import allure
@pytest.mark.usefixtures("one_time_set_up", "set_up")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, one_time_set_up):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = AssertStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUP(self):
        self.nav.navigate_to_all_courses()

    @data(*get_csv_data("testdata.csv"))
    @unpack
    @allure.feature()
    @allure.story()
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVC):
        self.courses.click_all_courses_tab()
        result1 = self.courses.enter_course_name(courseName)
        self.ts.mark(result1, "enter_course_name verification")
        result2 = self.courses.select_course_to_enroll(courseName)
        self.ts.mark(result2, "select_course verification")
        result3 = self.courses.enroll_course(num=ccNum, exp=ccExp, cvc=ccCVC)
        self.ts.mark(result3, "enroll_course verification")
        result4 = self.courses.verify_enroll_failed()
        self.ts.mark_final("test_invalidEnrollment", result4, "invalidEnrollment verification")
