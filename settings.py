import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
LOG_DIR = os.environ.get("LOG_DIR")

# TARGET_TAG_DICT = {'御朱印': 5, 'スイーツ女子': 5, '40代ママ': 5, '50代ライフスタイル': 5}
TARGET_TAG_DICT = {'御朱印': 2}
