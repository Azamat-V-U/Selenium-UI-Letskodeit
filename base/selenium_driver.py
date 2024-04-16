import traceback
from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging
import time
import os

class SeleniumDriver():
    log = cl.custom_logger((logging.DEBUG))

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, resultMessage):
        """
        Takes screenshot of the current open web page
        """
        filename = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "..//screenshots/"
        relative_file_name = screenshot_directory + filename
        current_directory = os.path.dirname(__file__)
        destination_file = os.path.join(current_directory, relative_file_name)
        destination_directory = os.path.join(current_directory, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to the directory" + destination_file)
        except:
            self.log.error("### An exception had occurred when it's being taken the screenshot")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        elif locator_type == "tag_name":
            return By.TAG_NAME
        else:
            self.log.info("Locator type " + locator_type +
                          " not correct/supported")
        return False

    def get_element(self, locator, locator_type):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info("Element is found with locator" + locator +
                          " and locatorType: " + locator_type)
        except:
            self.log.info("Exception: Element isn't found with locator: " + locator +
                          "and locatorType: " + locator_type)
        return element

    def get_element_list(self, locator, locator_type="", element=""):
        """
        NEW METHOD
        Get list of elements
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            self.log.info("Element list found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        except:
            self.log.info("Element list not found with locator: " + locator +
                          " and  locatorType: " + locator_type)
        return element

    def element_click(self, locator="", locatorType="xpath", element=None):
        try:
            if locator:
                element = self.get_element(locator, locatorType)
            element.click()
            self.log.info("Clicked on the element with locator: " + locator +
                          "locatorType: " + locatorType)
            return True
        except:
            self.log.info("Exception: Cannot click on the element with locator" + locator +
                          "locatorType: " + locatorType)
            print_stack()
            return False

    def send_keys(self, data, locator="", locatorType="xpath", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.get_element(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
            return True

        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            return False

    def send_keys_when_ready(self, data, locator="", locatorType="xpath"):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            by_type = self.get_by_type(locatorType)
            self.log.info("Waiting for maximum :: " + str(25) +
                          " :: seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=25,
                                 poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((by_type, locator)))
            self.log.info("Element appeared on the web page")
            element.click()
            element.send_keys(data)

            if element.get_attribute("value") != data:
                self.log.debug("Text is not sent by xpath in field so i will try to send string char by char!")
                element.clear()
                for i in range(len(data)):
                    element.send_keys(data[i] + "")
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Element not appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def drop_down_select(self, locator="", locatorType=""):

        element = self.get_element(locator, locatorType)

        try:
            if element:
                sel = Select(element)
                options = sel.options
                for index in range(len(options)):
                    sel.select_by_index(index)
                    time.sleep(1)
                self.log.info("All elements are selected by index")
                return True
            else:
                self.log.info("Elements can not be selected")
                return False
        except:
            self.log.error("Exception: Elements can not be selected")
            return False

    def select_elements(self, locator="", locatorType=""):

        try:
            element_list = self.get_element_list(locator, locatorType)
            if element_list is not None:
                size = len(element_list)
                self.log.info("The size of the list is " + str(size))
                for element in element_list:
                    if not element.is_selected():
                        element.click()
                        time.sleep(1)
                self.log.info("Elements are selected")
                return True
            else:
                self.log.info("Elements can not be selected")
                return False

        except:
            self.log.error("An error occurred while selecting elements: ")
            return False

    def un_select_elements(self, locator="", locatorType=""):

        try:
            element_list = self.get_element_list(locator, locatorType)
            if element_list is not None:
                size = len(element_list)
                self.log.info("The size of the list is " + str(size))
                for element in element_list:
                    if element.is_selected():
                        element.click()
                        # time.sleep(1)
                self.log.info("Elements are unselected")
                return True
            else:
                self.log.info("Elements can not be unselected")
                return False

        except:
            self.log.error("An error occurred while selecting elements: ")
            return False

    def is_element_present(self, locator="", locatorType="xpath", element=None):
        """
        Check if element is present -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:
                element = self.get_element(locator, locatorType)
            if element is not None:
                self.log.info("Element present with locator: " + locator +
                              " locatorType: " + locatorType)
                return True
            else:
                self.log.info("Element not present with locator: " + locator +
                              " locatorType: " + locatorType)
                return False
        except:
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator="", locatorType="xpath", element=None):
        """
        NEW METHOD
        Check if element is displayed
        Either provide element or a combination of locator and locatorType
        """
        is_displayed = False
        try:
            if locator:  # This means if locator is not empty
                element = self.get_element(locator, locatorType)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info("Element is displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            else:
                self.log.info("Element isn't displayed with locator: " + locator +
                              " locatorType: " + locatorType)
            return is_displayed
        except:
            self.log.info("Exception: Element not found")
            return False

    def is_element_selected(self, locator="", locatorType="id", element=None):
        is_selected = None
        try:
            if locator:
                element = self.get_element(locator, locatorType)
            if element is not None:
                is_selected = element.is_selected()
                self.log.info("Element is selected with locator: " + locator +
                              "locatorType: " + locatorType)
            else:
                self.log.info("Element is not selected with locator: " + locator +
                              "locatorType: " + locatorType)
            return is_selected
        except:
            self.log.info("Element is not selected")
            return False

    def element_list_presence_check(self, locator, byType):
        """
        Check if elementList is present
        """
        try:
            element_list = self.driver.find_elements(byType, locator)
            if len(element_list) > 0:
                self.log.info("ElementList present with locator: " + locator +
                              " locatorType: " + str(byType))
                return True
            else:
                self.log.info("ElementList not present with locator: " + locator +
                              " locatorType: " + str(byType))
                return False
        except:
            self.log.info("ElementList not found")
            return False

    def wait_for_element(self, locator, locatorType="xpath",
                         timeout=10, pollFrequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout=timeout,
                                 poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def web_scroll(self, direction="up"):
        """
        NEW METHOD
        """
        if direction == "up":
            # Scroll Up
            self.driver.execute_script("window.scrollBy(0, -1000);")

        if direction == "little up":
            # Scroll a little up
            self.driver.execute_script("window.scrollBy(0, -500);")

        if direction == "down":
            # Scroll Down
            self.driver.execute_script("window.scrollBy(0, 700);")

        if direction == "little down":
            # Scroll a little down
            self.driver.execute_script("window.scrollBy(0, 200);")

    def switch_to_frame_by_index(self, locator, locatorType="xpath"):
        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """

        result = False
        try:
            iframe_list = self.get_element_list("//iframe", locator_type="xpath")
            self.log.info("Length of an iframe list")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switch_to_frame(index=iframe_list[i])
                result = self.is_element_present(locator, locatorType)
                if result:
                    self.log.info("iframe index is: ")
                    self.log.info(str(i))
                    break
                self.switch_to_default_content()
            return result
        except:
            self.log.info("iFrame index isn't found")
        return result

    def switch_to_frame(self, id="", name="", index=""):
        """
        Switch to iframe using element locator inside the iframe
                Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
            self.log.info("Switched to frame with id")
        if name:
            self.driver.switch_to.frame(name)
            self.log.info("Switched to frame with name")
        if index:
            self.log.info("Switched to frame with index")
            self.log.info(str(index))
            self.driver.switch_to.frame(index)

    def switch_to_window(self, locator, locatorType):
        try:
            parent_handle = self.driver.current_window_handle
            self.log.info("Parent handle is found: " + parent_handle)
            element = self.get_element(locator, locatorType)
            element.click()
            time.sleep(3)
            handles = self.driver.window_handles
            for handle in handles:
                self.log.info("Handle: " + handle)
                if handle not in parent_handle:
                    self.driver.switch_to.window(handle)
                    self.log.info("Switched to the new window" + handle)
                    time.sleep(3)
                    if self.driver.current_window_handle == handle:
                        return True
                    else:
                        self.log.error("Failed to switch to the window")
                        return False
            return False
        except Exception as e:
            self.log.info(f"Exception Window switcher: {str()}")
            return False

    def switch_to_tab(self, locator, locatorType):
        try:
            parent_handle = self.driver.current_window_handle
            self.log.info("Parent handle is found: " + parent_handle)
            element = self.get_element(locator, locatorType)
            element.click()
            time.sleep(3)
            handles = self.driver.window_handles
            for handle in handles:
                self.log.info("Handle: " + handle)
                if handle not in parent_handle:
                    self.driver.switch_to.window(handle)
                    self.log.info("Switched to the new window" + handle)
                    time.sleep(3)
                    if self.driver.current_window_handle == handle:
                        return True
                    else:
                        self.log.error("Failed to switch to the window")
                        return False
            return False
        except Exception as e:
            self.log.info(f"Exception tab switcher: {str(e)}")
            return False

    def switch_to_alert(self, locator="", locatorType=""):

        try:
            if locator:
                element = self.get_element(locator, locatorType)
                element.click()
                time.sleep(2)
                alert = self.driver.switch_to.alert
                alert.accept()
                self.log.info("Alert is confirmed")
                return True
            else:
                self.log.info("Can't switch to alert")
                return False
        except Exception as e:
            self.log.info(f"Exception switch to Alert {str(e)}: ")
            return False

    def switch_to_confirm(self, locator="", locatorType=""):

        try:
            if locator:
                element = self.get_element(locator, locatorType)
                element.click()
                time.sleep(2)
                alert = self.driver.switch_to.alert
                alert.dismiss()
                self.log.info("Confirmation is canceled")
                return True
            else:
                self.log.info("Can't switch to confirmation")
                return False

        except Exception as e:
            self.log.info(f"Exception switch to confirm : {str(e)}")
            return False

    def hover_mouse_over(self, locator="", locatorType=""):

        element = self.get_element(locator, locatorType)
        item_to_click = ".//div[@class='mouse-hover-content']//a[text()='Reload']"

        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(element).perform()
            self.log.info("Mouse hovered")
            time.sleep(3)
            reload_item = self.get_element(item_to_click, locator_type="xpath")
            actions.move_to_element(reload_item).click().perform()
            time.sleep(3)
            self.log.info("Item clicked")
            return True
        except Exception as e:
            self.log.error(f"Failed to click on the item: {str(e)}")
            return False

    def switch_to_default_content(self):
        """
         Switch to default content
        Parameters:
        None
        Returns:
        None
        Exception:
        None
        :return:
        """
        self.driver.switch_to.default_content()
        self.log.info("Switched to default content")

    def get_element_attribute_value(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.get_element(locator=locator, locator_type=locatorType)
        value = element.get_attribute(attribute)
        return value

    def is_element_enabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.get_element(locator, locator_type=locatorType)
        enabled = False
        try:
            attribute_value = self.get_element_attribute_value(element=element, attribute="disabled")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is disabled")
        except:
            self.log.error("Element :: " + info + "' state could not be found")
        return enabled







