import json
from ntpath import basename

from Data.Keywords import data as keywords
from Data.Units import data as units
from HELP.file_tool import get_file_from_folder


def main(text):
    print(keywords)
    print(units)
    return {}


if __name__ == '__main__':
    ocr_files = get_file_from_folder("../Data/ocr_text")
    correct_files = get_file_from_folder("../Data/correct_text")
    for path in ocr_files:
        file_name = basename(path)
        ocr_file = open(path, "r", encoding="utf8")
        ocr_text = ocr_file.read()
        ocr_file.close()
        ocr_json = main(ocr_text)
        with open(f'../Data/nlp_ocr_text/mahad/{file_name}', 'w', encoding="utf8") as json_file:
            json.dump(ocr_json, json_file)
    for path in correct_files:
        file_name = basename(path)
        correct_file = open(path, "r", encoding="utf8")
        correct_text = correct_file.read()
        correct_file.close()
        correct_json = main(correct_text)
        with open(f'../Data/nlp_correct_text/mahad/{file_name}', 'w', encoding="utf8") as json_file:
            json.dump(correct_json, json_file)

