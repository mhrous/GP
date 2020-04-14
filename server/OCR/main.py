import pytesseract

from OCR.post_processing import post_processing
from OCR.pre_processing import pre_processing


def pytesseract_ocr(image):
    custom_config = r'-l eng+ara'
    return pytesseract.image_to_string(image, config=custom_config)


def ocr(image_path):
    process_image = pre_processing(image_path)
    ocr_res = pytesseract_ocr(process_image)
    process_res = post_processing(ocr_res)
    return process_res
