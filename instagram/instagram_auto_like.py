import chromedriver_binary
from selenium import webdriver
import time


class InstagramAutoLike:
    driver: webdriver
    logger = None
    done_count = 0
    current_tag_count = 0

    def __init__(self, driver: webdriver, logger):
        self.driver = driver
        self.logger = logger

    def auto_like(self, tag_dict: dict):
        time.sleep(5)
        self.logger.info('自動いいね！を開始します。')
        for tag, count in tag_dict.items():
            self.__search_and_like(tag=tag, count=count)
        self.logger.info(f'自動いいね！を終了しました。実施件数 : {self.done_count}')

    def __search_and_like(self, tag: str, count: int):
        self.logger.info(f'START : タグ「{tag}」')
        self.current_tag_count = 0

        for _ in range(3):
            try:
                time.sleep(5)
                self.__search_tag(tag)
                time.sleep(5)
                self.__add_like(count)
            except Exception as e:
                self.logger.error('いいね実行中にエラーが発生しました。3回まで繰り返します。')
                self.logger.error(e)
            else:
                break
        else:
            self.logger.error(f'タグ「{tag}」の実行中に3回エラーが発生したため、このタグのいいねを終了します。')

        self.logger.info(f'END : タグ「{tag}」')

    def __search_tag(self, tag: str):
        self.logger.info(f'タグ「{tag}」の検索を開始します。')
        self.driver.get(f'https://www.instagram.com/explore/tags/{tag}/')
        time.sleep(10)
        self.logger.info(f'タグ「{tag}」の検索を完了しました。')

    def __add_like(self, count: int):

        # 最新の最初の投稿を表示
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]').click()

        # 指定回数いいねを繰り返す
        while self.current_tag_count < count:
            time.sleep(15)
            like_button = self.driver.find_element_by_xpath(
                '/html/body/div[6]/div[2]/div/article/div/div[2]/div[2]/section[1]/span[1]/button')
            target_svg = like_button.find_elements_by_tag_name("svg")
            target_svg_label = target_svg[0].get_attribute("aria-label")
            if target_svg_label == 'いいね！':
                like_button.click()
                self.current_tag_count += 1
                self.logger.info(f'いいね！しました。{self.done_count + self.current_tag_count}回目')
                time.sleep(15)
            self.driver.find_element_by_xpath('/html/body/div[6]/div[1]/div/div/a[2]').click()
        self.done_count += self.current_tag_count

        # 投稿を閉じる
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[6]/div[3]/button').click()
