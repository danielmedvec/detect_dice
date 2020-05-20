import cv2
import os
import ntpath

from skimage import io
from settings import IMAGE_INPUT_DIR


def get_image_from_url(https_url):

    file_name = ntpath.basename(https_url)
    file_path = os.path.join(IMAGE_INPUT_DIR, file_name)

    http_frame = io.imread(https_url)
    image = cv2.cvtColor(http_frame, cv2.COLOR_BGR2RGB)
    cv2.imwrite(file_path, image)

    return file_path


if __name__ == '__main__':

    get_image_from_url(https_url="imgur.com/dice.png")
