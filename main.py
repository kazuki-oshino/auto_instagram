import instagram
import log_util


if __name__ == '__main__':
    # setting logger
    logger = log_util.setup_logger('/Users/kazuki/PycharmProjects/auto_instagram/log/log.log')

    # web_driverを生成
    driver_util = instagram.driver_util.DriverUtil()

    # Instagramへのアクセス
    instagram_common = instagram.instagram_common.InstagramCommon(driver_util.get_driver(), logger)
    instagram_common.access_instagram()
