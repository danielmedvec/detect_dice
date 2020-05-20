import os

from flask import Flask, request, send_file
from src.pip_dice.grouper import extract_pips_each_dice
from src.image.extractor import get_image_from_url
from utils.folder_file_manager import log_print
from settings import IMAGE_SAVE_DIR, WEB_SERVER, SERVER_PORT, SERVER_HOST

app = Flask(__name__)


@app.route('/detect', methods=['GET'])
def run():

    try:

        frame_url = request.args.get('img')
        frame_path = get_image_from_url(https_url=frame_url)
        result = extract_pips_each_dice(frame_path=frame_path)

        return result

    except Exception as e:
        log_print(info_str=e)
        response = None

        return response


@app.route('/saved', methods=['GET'])
def get_saved_image():
    try:

        frame_name = request.args.get('name')
        frame_path = os.path.join(IMAGE_SAVE_DIR, frame_name)

        return send_file(frame_path, as_attachment=True)

    except Exception as e:
        log_print(info_str=e)
        response = None

        return response


if __name__ == '__main__':

    if WEB_SERVER:
        app.run(debug=True, host=SERVER_HOST, port=SERVER_PORT)
    else:
        app.run()
