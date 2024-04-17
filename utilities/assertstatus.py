"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""

import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
from traceback import print_stack


class AssertStatus(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(AssertStatus, self).__init__(driver)
        self.resultList = []

    def set_result(self, result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info(resultMessage + " Pass")
                    self.resultList.clear()
                else:
                    self.resultList.append("FAIL")
                    self.log.error(resultMessage + " Fail")
                    # self.take_screenshot(resultMessage)
                    self.resultList.clear()
            else:
                self.resultList.append("FAIL")
                self.log.error(resultMessage + " Result is not defined")
                self.log.info(resultMessage)
                # self.take_screenshot(resultMessage)
                self.resultList.clear()
        except:
            self.resultList.append("FAIL")
            self.log.error(resultMessage + " Exception occurred")
            self.log.info(resultMessage)
            # self.take_screenshot(resultMessage)
            self.resultList.clear()
            print_stack()

    # AssertStatus.mark.pass or fail(This method applies to the verification point of the testcase)
    def mark(self, result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, resultMessage)

    # AssertStatus.markFinal.pass or fail(This method applies to the end of the testcase)
    def mark_final(self, testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName + "### TEST IS FAILED")
            self.resultList.clear()
            assert True == False
        else:
            self.log.info(testName + "### TEST IS PASSED")
            self.resultList.clear()
            assert True == True
