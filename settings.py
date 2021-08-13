import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
LOG_DIR = os.environ.get("LOG_DIR")
