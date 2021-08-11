import instagram
import log_util
import settings

if __name__ == '__main__':
    # setting logger
    logger = log_util.setup_logger(settings.LOG_DIR)

    # web_driverを生成
    driver_util = instagram.driver_util.DriverUtil()

    # Instagramへのアクセス
    instagram_common = instagram.instagram_common.InstagramCommon(driver_util.get_driver(), logger)
    instagram_common.access_instagram()

    # 自動いいね処理
    auto_like = instagram.instagram_auto_like.InstagramAutoLike(driver_util.get_driver(), logger)
    auto_like.auto_like(settings.TARGET_TAG_DICT)

    # ログアウト
    instagram_common.log_out_instagram()

    # quit driver
    del driver_util
