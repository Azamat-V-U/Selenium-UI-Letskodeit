"""
@package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""

import time
import traceback
import utilities.custom_logger as sl
import random, string
import logging

class Util():

    log = sl.custom_logger(logging.INFO)

    def verify_text_contains(self, actualText, expectedText):
        self.log.info("Actual text from Application Web UI :: " + actualText)
        self.log.info("Expected text from Application Web UI :: " + expectedText)
        if actualText.lower() in expectedText.lower():
            self.log.info("Verification contains !!!")
            return True
        else:
            self.log.info("Verification doesn't contain !!!")
            return False