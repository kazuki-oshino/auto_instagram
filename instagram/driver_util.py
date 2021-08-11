import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class DriverUtil:

    driver = None

    def __init__(self):
        self.__prepare_driver()

    def __prepare_driver(self):
        options = Options()
        options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=options)

    def get_driver(self):
        return self.driver
