import cv2
import numpy as np


def read_image(image_path):
    return cv2.imread(image_path)


def func2(obj):
    kernel = np.ones((2, 2), np.uint8)
    opening = cv2.morphologyEx(obj, cv2.MORPH_OPEN, kernel)
    return opening


def pre_processing(image_path):
    image = read_image(image_path)
    res_2 = func2(image)

    return res_2
