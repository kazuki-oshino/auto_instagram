import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class InstagramAutoLike:
    driver: webdriver
    logger = None
    done_count = 0

    def __init__(self, driver: webdriver, logger):
        self.driver = driver
        self.logger = logger

    def auto_like(self, tag_dict: dict):
        time.sleep(5)
        self.logger.info('自動いいね！を開始します。')
        for tag, count in tag_dict.items():
            self.logger.info(f'START : タグ「{tag}」')
            time.sleep(5)
            self.__search_tag(tag)
            time.sleep(5)
            self.__add_like(count)
            self.logger.info(f'END : タグ「{tag}」')
        self.logger.info(f'自動いいね！を終了しました。実施件数 : {self.done_count}')

    def __search_tag(self, tag: str):
        self.logger.info(f'タグ「{tag}」の検索を開始します。')
        self.driver.get(f'https://www.instagram.com/explore/tags/{tag}/')
        time.sleep(10)
        self.logger.info(f'タグ「{tag}」の検索を完了しました。')

    def __add_like(self, count: int):
        # 最新の最初の投稿を表示
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]').click()

        # 指定回数いいねを繰り返す
        current_done_like = 0
        while current_done_like < count:
            time.sleep(5)
            like_button = self.driver.find_element_by_xpath(
                '/html/body/div[6]/div[2]/div/article/div[3]/section[1]/span[1]/button')
            target_svg = like_button.find_elements_by_tag_name("svg")
            target_svg_label = target_svg[0].get_attribute("aria-label")
            if target_svg_label == 'いいね！':
                like_button.click()
                current_done_like += 1
                self.logger.info(f'いいね！しました。{self.done_count + current_done_like}回目')
            time.sleep(5)
            self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/a[2]').click()

        self.done_count += current_done_like

        # 投稿を閉じる
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/button').click()
