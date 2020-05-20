import cv2


def detect_all_pips(frame_path):

    pip_coordinates = []

    frame = cv2.imread(frame_path)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(frame_gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=15, minRadius=6, maxRadius=11)
    for circle in circles[0]:
        black_roi = frame_gray[int(circle[1] - circle[2]):int(circle[1] + circle[2]),
                               int(circle[0] - circle[2]):int(circle[0] + circle[2])]
        white_roi = frame_gray[int(circle[1] - 2 * circle[2]):int(circle[1] + 2 * circle[2]),
                               int(circle[0] - 2 * circle[2]):int(circle[0] + 2 * circle[2])]
        black_pixels = len(black_roi[black_roi < 100])
        white_pixels = len(white_roi[white_roi > 130])
        # print(black_pixels, white_pixels)
        if black_pixels < 50 or white_pixels < 500:
            continue
        pip_coordinates.append([circle[0], circle[1]])
        cv2.circle(frame, (int(circle[0]), int(circle[1])), int(circle[2]), (0, 0, 255), 2)
    # cv2.imshow("dice frame", frame)
    # cv2.waitKey()

    return pip_coordinates, frame


if __name__ == '__main__':
    detect_all_pips(frame_path="")
