from ntpath import basename

from HELP.file_tool import get_file_from_folder
from OCR.main import ocr


def save_file(name, text, path):
    with open(f'{path}{name}', "w+") as file:
        file.write(text)

        pass


def ocr_for_all_image():
    path = "../static"
    image_path_list = get_file_from_folder(path)
    for image in image_path_list:
        file_name = basename(image).split('.')[0] + ".txt"
        file_text = ocr(image)

        save_file(name=file_name, text=file_text, path="../Data/ocr_text/")


def create_empty_file():
    path = "../static"
    image_path_list = get_file_from_folder(path)
    for image in image_path_list:
        file_name = basename(image).split('.')[0]
        f1 = open(f"../Data/correct_text/{file_name}.txt", "w")
        f2 = open(f"../Data/ocr_text/{file_name}.txt", "w")

        f1.close()
        f2.close()


if __name__ == '__main__':
    ocr_for_all_image()
    pass
