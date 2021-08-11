import chromedriver_binary
from selenium import webdriver
import time
import settings


class InstagramCommon:

    driver: webdriver
    logger = None
    username = ''
    password = ''

    def __init__(self, driver: webdriver, logger):
        self.driver = driver
        self.logger = logger
        self.username = settings.USERNAME
        self.password = settings.PASSWORD

    def access_instagram(self):
        self.logger.info('instagramへのアクセスを開始します。')
        self.driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        time.sleep(1)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(1)
        self.logger.info('instagramへのアクセスを完了しました。')

