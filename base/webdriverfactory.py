from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


class WebDriverFactory:

    def get_web_driver_instance(self):
        options = Options()
        options.add_argument("--headless")
        base_url = "https://www.letskodeit.com/"
        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(base_url)
        return driver
