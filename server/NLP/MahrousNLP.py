import copy
import json
import re
from ntpath import basename

from fuzzywuzzy import process

from Data.keywords import KEYWORDS, PROBLEM_TYPE, PHYSICAL_AMOUNT, get_all_units, get_term_form_keywords
from HELP.file_tool import get_file_from_folder
from constants import FUNCTION_AMPLITUDE_FOR_PENDULUMS

THRESHOLD = 85
KEYWORDS_LIST = KEYWORDS.keys()

ALL_UNITS = get_all_units(KEYWORDS)
ALL_TERM = get_term_form_keywords(KEYWORDS)


def first_list_in_second_list(a, b):
    return set(a).issubset(set(b))


def remove_duplicate_from_array(array):
    return list(set(array))


def link_keyword_with_symbols(data):
    def link_related_KEYWORDS_to_values(keywords, value):
        for key in keywords:
            keyword = KEYWORDS[key]
            if keyword['type'] == PHYSICAL_AMOUNT and value in keyword['symbols']:
                return key

        return None

    def get_value_and_unit(right):
        for item in ALL_UNITS:
            if item in right:
                index = right.index(item)
                unit = right[index:]
                value = right[:index]
                if item != unit:
                    continue
                return value, unit
        return right, None

    res = []
    for item in data:
        obj = copy.deepcopy(item)
        state = []
        symbols = obj['symbols']
        keyword = obj['keyword']
        for symbol in symbols:
            if '=' in symbol:
                [variable, right,*_] = symbol.split('=')
                value, unit = get_value_and_unit(right)
                keywordToValue = link_related_KEYWORDS_to_values(keyword, variable)
                state.append({'variable': variable, 'unit': unit, 'keyword': keywordToValue, 'value': value})

        used_keywords = [item['keyword'] for item in state]

        obj['state'] = state

        obj['non_used_keywords'] = [item for item in keyword if
                                    item not in used_keywords and KEYWORDS[item]['type'] == PHYSICAL_AMOUNT]

        res.append(obj)
    return res


def problem_classification(data):
    words = [
        (word, KEYWORDS[word][PROBLEM_TYPE])
        for line in data for word in line["keyword"]
        if PROBLEM_TYPE in KEYWORDS[word]
    ]
    words = [(word, _type) for word, type_list in words for _type in type_list]
    if len(words) == 0:
        return None
    res = {}
    rank_sum = 0
    for word, (_type, rank) in words:
        res[_type] = rank if _type not in res else res[_type] + rank
        rank_sum += rank

    return {_type: rank / rank_sum for _type, rank in res.items()}


def spilt_problem(text):
    '''
    :param text: نص المسالة
    :return: تقسيم المسالة الى نص وطلبات
    '''
    res = None
    if "مطلوب" not in text:
        res = re.split("\n\d[\s_-]", text)
    else:
        split_req = re.split("المطلوب", text)
        res = [split_req[0]] + re.split("\n\d[\s\-_]", split_req[1])

    return [item for item in res if re.search("[\w\d]", item) and len(item) > 1]


def get_symbols(array):
    '''
    :param array:  نص المسائلة والطلبات
    :return: نص المسائلة والطلبات وما يحتوا من متغيرات فيزيائية
    '''

    def remove_arabic(text):
        _array = [' ' if ord(item) > 500 else item for item in text]
        symbols_string = "".join(_array)
        symbols_list = re.split("   +", symbols_string)
        symbols_list = [re.sub("[\n\s]", "", item).lower() for item in symbols_list if re.search("[\w]", item)]
        return remove_duplicate_from_array(symbols_list)

    return [remove_arabic(item) for item in array]


def get_keywords(array):
    def remove_symbols(text):
        _array = [' ' if ord(item) < 500 else item for item in text]
        arabic_string = "".join(_array)
        arabic_list = re.split("   +", arabic_string)
        res = []
        for item in arabic_list:
            for txt in item.split(" "):
                if txt == "" or txt == "؟":
                    continue
                word, rank = process.extractOne(txt, KEYWORDS_LIST)
                if rank >= THRESHOLD:
                    res.append(word)

        for term in ALL_TERM:
            term_array = term.split(' ')
            if first_list_in_second_list(term_array, res):
                res.append(term)
                res = list(set(res) - set(term_array))

        return res

    return [remove_symbols(item) for item in array]


def handle_special_cases(item):
    obj = copy.deepcopy(item)
    keyword = obj['keyword']
    symbol = obj['symbols']
    state = obj['state']
    amplitude = "(x(max)?=)?\d*(\.\d*)?cos\(.*t.*\)"

    if re.search(amplitude, " ".join(symbol)):
        for item in state:
            if re.search(amplitude, item["value"]):
                item["keyword"] = FUNCTION_AMPLITUDE_FOR_PENDULUMS
    return obj


def main(text):
    text = f'''{text}'''
    array = spilt_problem(text)
    array_symbols = get_symbols(array)
    array_arabic = get_keywords(array)

    data = [
        {
            "type": "نص السوال" if i == 0 else f"{i} الطلب",
            "line": array[i],
            "keyword": array_arabic[i],
            "symbols": array_symbols[i]
        }
        for i in range(len(array))
    ]
    data = link_keyword_with_symbols(data)
    data = [handle_special_cases(item) for item in data]
    problem_type = problem_classification(data)

    return {"data": data, "problem_type": problem_type}


if __name__ == '__main__':
    ocr_files = get_file_from_folder("../Data/ocr_text")
    correct_files = get_file_from_folder("../Data/correct_text")
    for path in ocr_files:
        file_name = basename(path)
        ocr_file = open(path, "r", encoding="utf8")
        ocr_text = ocr_file.read()
        ocr_file.close()
        ocr_json = main(ocr_text)
        with open(f'../Data/nlp_ocr_text/mahrous/{file_name}', 'w', encoding="utf8") as json_file:
            json.dump(ocr_json, json_file)
    for path in correct_files:
        file_name = basename(path)
        correct_file = open(path, "r", encoding="utf8")
        correct_text = correct_file.read()
        correct_file.close()
        correct_json = main(correct_text)
        with open(f'../Data/nlp_correct_text/mahrous/{file_name}', 'w', encoding="utf8") as json_file:
            json.dump(correct_json, json_file)
