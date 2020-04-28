import json
import re
from ntpath import basename

from Data.Keywords import data as keywords
from Data.unit import data as unit
from HELP.file_tool import get_file_from_folder


def main(text):
    text = f'''{text}'''
    text = re.sub(r'\n|o|O|\(.*?\)', r'', text)

    pattern = r'([A-Za-z0-9^*/=)(\'\.\-\+]+)'
    data = re.findall(pattern, text)

    answers = []
    for match in data:
        if re.findall(r'a\.|b\.|c\.|d\.|a\)|b\)|c\)|d\)', match):
            answers.append(match)

    unit_value = quantites = res = []

    data = [i for i in data if i not in answers]
    unit_value = [i for i in data if re.match(r'^[0-9]+', i)]
    quantites = [i for i in data if i not in unit_value]
    finished_quantite = [re.findall(r'\S+\=\S+', i)[0] for i in quantites if len(re.findall(r'\S+\=\S+', i)) != 0]

    if len(finished_quantite) >= 0:
        for i in finished_quantite:
            quantites.remove(i)

    [res.append((i, '?')) for i in unit_value]
    [res.append(('?', i)) for i in quantites]

    new_res = []
    for quant_and_val in res:
        if quant_and_val[0] == '?':
            new_res.append((quant_and_val))
        else:
            for key, value in unit.data.items():
                for i in value['for']:
                    if re.sub(r'{}'.format(re.findall(r'^\d+\.\d+|^\d+', str(quant_and_val[0]))[0]), '',
                              quant_and_val[0]) == key:
                        new_res.append((quant_and_val[0], i['symbol']))

    if len(finished_quantite) > 1:
        for i in finished_quantite:
            i = re.split(r'=', i)
            new_res.append((i[1], i[0]))
    elif len(finished_quantite) == 1:
        finished_quantite = re.split(r'=', finished_quantite[0])
        new_res.append((finished_quantite[1], finished_quantite[0]))

    data_dicts = []
    quantity = Unit = sym = ''
    value = 0

    for quant_and_val in new_res:
        if quant_and_val[1] != '?' and quant_and_val[0] == '?':
            val = quant_and_val[0]
            Unit = quant_and_val[0]
            sym = quant_and_val[1]
            for key, value in unit.data.items():
                for i in value['for']:
                    if re.findall(r'[\D]+', str(quant_and_val[1]))[0] == i['symbol']:
                        quantity = i['name']

        elif quant_and_val[1] == '?' and quant_and_val[0] != '?':
            val = re.findall(r'^\d+\.\d+|^\d+', str(quant_and_val[0]))[0] if len(
                re.findall(r'^\d+', str(quant_and_val[0]))) != 0 else '?'
            Unit = re.sub(r'{}'.format(val), '', str(quant_and_val[0])) if val != '?' else '?'
            for key, value in unit.data.items():
                for i in value['for']:
                    if Unit == key:
                        quantity = i['name']
                        sym = i['symbol']
        else:

            val = re.findall(r'^\d+\.\d+|^\d+', str(quant_and_val[0]))[0] if len(
                re.findall(r'^\d+', str(quant_and_val[0]))) != 0 else '?'
            Unit = re.sub(r'{}'.format(val), '', str(quant_and_val[0])) if val != '?' else '?'
            sym = quant_and_val[1]
            for key, value in unit.data.items():
                for i in value['for']:
                    if quant_and_val[1] == i['symbol']:
                        quantity = i['name']

        dict1 = {'quantity': quantity, 'value': val, 'unit': Unit, 'symbol': sym}
        data_dicts.append(dict1)

    return data_dicts


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

