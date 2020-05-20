import os

from utils.folder_file_manager import make_directory_if_not_exists


CUR_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_SAVE_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'output'))
IMAGE_INPUT_DIR = make_directory_if_not_exists(os.path.join(CUR_DIR, 'input'))

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5000

WEB_SERVER = True
