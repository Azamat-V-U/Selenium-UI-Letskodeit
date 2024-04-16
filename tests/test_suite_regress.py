import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_tests import RegisterCoursesCSVDataTests

tc_1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc_2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)


smokeTest = unittest.TestSuite([tc_1, tc_2])

unittest.TextTestRunner(verbosity=2).run(smokeTest)
