from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def get_web_driver_instance(self):
        """
            Get WebDriver Instance based on the browser configuration

            Returns:
            'WebDriver Instance'
        """
        base_url = "https://www.letskodeit.com/"
        if self.browser == "chrome":
            driver = webdriver.Chrome()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)
        return driver


