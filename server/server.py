import base64
import json
import os
import random
from io import BytesIO
from ntpath import basename

from OCR.main import ocr
from NLP.MahrousNLP import main as nlp

from PIL import Image
from flask import Flask, jsonify, request
from flask_cors import CORS

from HELP.file_tool import get_file_from_folder
from constants import CONSTANTS

app = Flask(__name__, static_folder='static', static_url_path="/static")
CORS(app)


def save_file(name, text, path):
    with open(f'{path}{name}', "w+") as file:
        file.write(text)

        pass


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
        image_solve_file_path = f'./Data/solve/{image_name_without_addition}.txt'
        ocr_text = read_file(image_ocr_text_file_path)
        correct_text = read_file(image_correct_text_file_path)
        nlp_mahad_ocr_text = json.loads(read_file(image_nlp_mahad_ocr_text_file_path))
        nlp_mahad_correct_text = json.loads(read_file(image_nlp_mahad_correct_text_file_path))
        nlp_mahrous_ocr_text = json.loads(read_file(image_nlp_mahrous_ocr_text_file_path))
        nlp_mahrous_correct_text = json.loads(read_file(image_nlp_mahrous_correct_text_file_path))
        solve = json.loads(read_file(image_solve_file_path))

        result[image_name_without_addition] = {
            "correct_text": correct_text,
            "ocr_text": ocr_text,
            "image_path": image_path,
            "image_name": image_name,
            "nlp_mahad_ocr_text": nlp_mahad_ocr_text,
            "nlp_mahad_correct_text": nlp_mahad_correct_text,
            "nlp_mahrous_ocr_text": nlp_mahrous_ocr_text,
            "nlp_mahrous_correct_text": nlp_mahrous_correct_text,
            "solve": solve
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


@app.route('/', methods=['POST'])
def cameraapi():
    cwd = os.path.abspath(os.getcwd())
#     solution = {}
    image_data = request.json['image']
    name = str(f'{random.randint(0, 100000000000)}.png')
    img = Image.open(BytesIO(base64.b64decode(image_data.split(',')[1])))

    img_path = f'{cwd}/imageProcciessing/{name}'
    img.save(img_path)

    text = ocr(img_path)
    save_file(name=name[:-4]+'.txt', text=text, path=f"{cwd}/imageProcciessing/")
    nlp_result = nlp(text)
    quantitites = [item for data in nlp_result['data'] for item in data['symbols']]
    nlp_result['quantitites']=quantitites

    return jsonify(nlp_result)

@app.route("/solve")
def solve():

    new_quantitites = request.json['new_quantitites']
    obj = request.json['obj']

    return body


@app.route('/text', methods=['GET', 'POST'])
def textapi():
    solution = {}
    if request.method == 'POST':
        text = request.json["text"]
        grammar = request.json["grammar"]
        print(text, grammar)
        if (grammar == "Finder"):
            solution['result'] = tense_parser.find_tense_simple_form_str(text)
        elif (grammar == "Conjunction"):
            text, explain = GrammerSolver(text)
            solution['result'] = text
            solution['result way'] = explain
        else:
            solution['result'] = QuestionGenerater(f'''{text}.''')
        print(solution)
        return solution

    elif request.method == 'GET':
        return 'Hello'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=CONSTANTS['PORT'])
