import time
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util


class BasePage(SeleniumDriver):

    def __init__(self, driver):
        """
        BasePage class returns None
        :param driver:
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, titleToVerify):
        """
        Verify the page title
        :param titleToVerify:
        :return:
        """
        try:
            actual_title = self.get_title()
            time.sleep(3)
            return self.util.verify_text_contains(actual_title, titleToVerify)
        except:
            print("Failed to get page title")
            print_stack()
            return False





