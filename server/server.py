import json
from ntpath import basename

from flask import Flask, jsonify
from flask import request
from flask_cors import CORS

from HELP.file_tool import get_file_from_folder
from constants import CONSTANTS

app = Flask(__name__, static_folder='static', static_url_path="/static")
CORS(app)


@app.route("/problems", methods=['GET'])
def get_problems():
    def read_file(path="", _type="txt"):
        file = open(path, "r", encoding="utf8")
        data = file.read()
        file.close()
        return data

    image_path_list = get_file_from_folder('./static')

    result = {}
    for image in image_path_list:
        image_name = basename(image)
        image_name_without_addition = image_name.split('.')[0]
        image_path = f'http://localhost:3001/static/{image_name}'
        image_ocr_text_file_path = f'./Data/ocr_text/{image_name_without_addition}.txt'
        image_correct_text_file_path = f'./Data/correct_text/{image_name_without_addition}.txt'
        image_nlp_mahad_ocr_text_file_path = f'./Data/nlp_ocr_text/mahad/{image_name_without_addition}.txt'
        image_nlp_mahad_correct_text_file_path = f'./Data/nlp_correct_text/mahad/{image_name_without_addition}.txt'
        image_nlp_mahrous_ocr_text_file_path = f'./Data/nlp_ocr_text/mahrous/{image_name_without_addition}.txt'
        image_nlp_mahrous_correct_text_file_path = f'./Data/nlp_correct_text/mahrous/{image_name_without_addition}.txt'
        ocr_text = read_file(image_ocr_text_file_path)
        correct_text = read_file(image_correct_text_file_path)
        nlp_mahad_ocr_text = json.loads(read_file(image_nlp_mahad_ocr_text_file_path))
        nlp_mahad_correct_text = json.loads(read_file(image_nlp_mahad_correct_text_file_path))
        nlp_mahrous_ocr_text = json.loads(read_file(image_nlp_mahrous_ocr_text_file_path))
        nlp_mahrous_correct_text = json.loads(read_file(image_nlp_mahrous_correct_text_file_path))
        result[image_name_without_addition] = {
            "correct_text": correct_text,
            "ocr_text": ocr_text,
            "image_path": image_path,
            "image_name": image_name,
            "nlp_mahad_ocr_text": nlp_mahad_ocr_text,
            "nlp_mahad_correct_text": nlp_mahad_correct_text,
            "nlp_mahrous_ocr_text": nlp_mahrous_ocr_text,
            "nlp_mahrous_correct_text": nlp_mahrous_correct_text
        }
    return jsonify(result)

    pass


@app.route('/problems', methods=['POST'])
def set_problems():
    data = request.json['body']

    image_name_without_addition = data["image_name"].split('.')[0]
    image_correct_text_file_path = f'./Data/correct_text/{image_name_without_addition}.txt'
    with open(image_correct_text_file_path, 'w', encoding="utf8") as file:
        file.write(data['correct_text'])

    return jsonify(data)


@app.route("/keywords", methods=["GET"])
def get_keywords():
    pass


@app.route("/keywords", methods=["POST"])
def set_keywords():
    pass


if __name__ == '__main__':
    app.run(port=CONSTANTS['PORT'])
