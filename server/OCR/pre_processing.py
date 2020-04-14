import cv2


def read_image(image_path):
    return cv2.imread(image_path)


def func2(obj):
    return obj


def pre_processing(image_path):
    image = read_image(image_path)
    res_2 = func2(image)

    return res_2
