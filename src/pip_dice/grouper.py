import cv2
import ntpath
import os

from sklearn.cluster import AgglomerativeClustering
from src.pip_dice.detector import detect_all_pips
from settings import IMAGE_SAVE_DIR


def extract_pips_each_dice(frame_path):

    dice_info = {}
    file_name = ntpath.basename(frame_path)
    save_file_path = os.path.join(IMAGE_SAVE_DIR, file_name)

    pips, pips_frame = detect_all_pips(frame_path=frame_path)
    height, width = pips_frame.shape[:2]
    cluster = AgglomerativeClustering(n_clusters=12, affinity='euclidean', linkage='ward')
    cluster.fit_predict(pips)
    pip_labels = cluster.labels_

    dice_info["dice_amt_found"] = 12
    dice_info["save_image_name"] = file_name
    cv2.putText(pips_frame, "dice_amt_found: 12", (10, 30), cv2.FONT_HERSHEY_TRIPLEX, height / 1000,
                (0, 255, 0), 1)
    for i in range(12):
        each_pip = len(pip_labels[pip_labels == i])
        dice_info["dice_{}".format(i + 1)] = each_pip
        cv2.putText(pips_frame, "dice_{}: {}".format(i + 1, each_pip), (10, 30 * (i + 2)), cv2.FONT_HERSHEY_TRIPLEX,
                    height / 1000, (0, 255, 0), 1)

    cv2.imwrite(save_file_path, pips_frame)

    return dice_info


if __name__ == '__main__':

    extract_pips_each_dice(frame_path="/media/mensa/Data/Task/DiceDetector/0PeZbb3.png")
