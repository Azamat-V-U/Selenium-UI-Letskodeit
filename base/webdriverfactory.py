from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def get_web_driver_instance(self):
        """
            Get WebDriver Instance based on the browser configuration

            Returns:
            'WebDriver Instance'
        """
        options = Options()
        options.add_argument("--headless")
        base_url = "https://www.letskodeit.com/"
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=options)
        # if self.browser == "chrome":
        #     # driver = webdriver.Chrome()
        #     driver = webdriver.Chrome(options=options)
        # elif self.browser == "firefox":
        #     # driver = webdriver.Firefox()
        #     driver = webdriver.Firefox(options=options)
        # else:
        #     # driver = webdriver.Chrome()
        #     driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)
        return driver