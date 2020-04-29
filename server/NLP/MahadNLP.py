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
    if re.match(r'المطلوب', ''.join(data)):
        problem = text.split(sep="المطلوب")
        answers = problem[-1]
    else:
        for match in data:
            if re.findall(r'a.|b.|c.|d.|a\)|b\)|c\)|d\)', match):
                answers.append(match)

    unit_value = quantites = []
    res = {}

    data = [i for i in data if i not in answers]
    unit_value = [i for i in data if re.match(r'^[0-9]+', i)]
    quantites = [i for i in data if i not in unit_value]
    finished_quantite = [re.match(r'\w+\=\d+(.*)?', i).group(0) for i in quantites if
                         re.match(r'\w+\=\d+(.*)?', i) != None]

    if len(finished_quantite) >= 0:
        for i in finished_quantite:
            quantites.remove(i)

    while len(quantites) > len(unit_value):
        unit_value.append('?')
    while len(unit_value) > len(quantites):
        quantites.append('?')

    res = dict(zip(unit_value, quantites))

    unknown_value = ''

    for k, v in res.items():
        for key, value in unit.items():
            for i in value['for']:
                if len(re.findall(r'[\D]+', str(k))) == 0 and re.findall(r'[\D]+', str(k))[0] != key and len(re.findall(r'[\D]+', str(v))) == 0 and re.findall(r'[\D]+', str(v))[0] != i['symbol'] and k == '?':
                    res[k] = i['symbol']
                    unknown_value = v

    if len(finished_quantite) == 1:
        finished_quantite = re.split(r'=', finished_quantite[0])
        res[finished_quantite[1]] = finished_quantite[0]
    elif len(finished_quantite) > 1:
        for i in finished_quantite:
            i = re.split(r'=', i)
            res[i[1]] = i[0]

    if unknown_value != '?' and unknown_value != '':
        res[unknown_value] = '?'

    data_dicts = []
    quantity = Unit = sym = ''
    value = 0

    for k, v in res.items():
        if v != '?' and k == '?':
            val = k
            Unit = k
            sym = v
            for key, value in unit.items():
                for i in value['for']:
                    if re.findall(r'[\D]+', str(v))[0] == i['symbol']:
                        quantity = i['name']
        elif v != '?' and k != '?':
            val = re.findall(r'^\d+', str(k))[0]
            Unit = re.findall(r'\D+/.*|\D+\^\d|[\D]+', str(k))[0]
            sym = v
            for key, value in unit.items():
                for i in value['for']:
                    if Unit == key:
                        quantity = i['name']
        elif v == '?' and k != '?':
            val = re.findall(r'^\d+', str(k))[0]
            Unit = re.findall(r'\D+/.*|\D+\^\d|[\D]+', str(k))[0]
            for key, value in unit.items():
                for i in value['for']:
                    if Unit == key:
                        quantity = i['name']
                        sym = i['symbol']
        else:
            val = v
            Unit = v
            sym = k
            for key, value in unit.items():
                for i in value['for']:
                    if k == i['symbol']:
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

