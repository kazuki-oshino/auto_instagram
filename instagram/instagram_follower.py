import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import settings


class InstagramFollower:
    driver: webdriver
    logger = None
    username = ''

    def __init__(self, driver: webdriver, logger):
        self.driver = driver
        self.logger = logger
        self.username = settings.USERNAME

    def access_my_page(self):
        time.sleep(2)
        self.logger.info('MyPageに遷移します。')
        self.driver.get(f'https://www.instagram.com/{self.username}/')
        time.sleep(2)
        self.logger.info('MyPageに遷移しました。')

    def get_follower(self) -> list:
        time.sleep(2)
        self.logger.info('フォロワーの取得を開始します。')

        # フォロワー覧を開く
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

        # フォロワー一覧を取得
        time.sleep(1)
        follower_list = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')

        time.sleep(1)
        # TODO(kazuki): scroll ができない！
        follower_list.click()
        follower_list.send_keys(Keys.PAGE_DOWN)

        time.sleep(2)
        self.logger.info('フォロワーの取得が完了しました。')
        return []
