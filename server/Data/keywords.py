PHYSICAL_AMOUNT = "مقدار فيزيائي"
UNIT_TYPE = "نوع واحدة"
PROBLEM_TYPE = "نوع مسالة"
WAVES = "امواج"
LIQUIDS = "سوائل"
PENDULUMS = "نواسات"
MAX = 1000
MED = 100
MIN = 10
KEYWORDS = {
    "خزان": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(LIQUIDS, MED)]
    },
    "نواس مرن": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "نواس": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(PENDULUMS, MAX)]
    },
    "مرن": {
        "type": PROBLEM_TYPE,

        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "توافقية": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "سعة اهتزاز": {

        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m"],
        "symbols": ["x", "xmax"],
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "سعة": {
        "type": "",
        PROBLEM_TYPE: [(PENDULUMS, MIN), (LIQUIDS, MIN)]
    },
    "اهتزاز": {
        "type": "",
        PROBLEM_TYPE: [(PENDULUMS, MIN), (LIQUIDS, MIN)]
    },
    "مبدا الزمن": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["s"],
        "symbols": ["t"],
        "value": 0,

    },
    "الزمن": {

        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["s"],
        "symbols": ["t"],
        "value": ""
    },
    "مبدا": {
        "type": "",
        "value": ""
    },
    "لحظة مرور": {
        "type": "",
        "value": ""
    },
    "مرور": {
        "type": "",
        "value": ""
    },
    "لحظة": {
        "type": "",
        "value": ""
    },
    "افقي": {
        "type": "",
    },
    "شاقولي": {
        "type": "",
    },
    "تابعه الزمني": {
        "type": "",
        PROBLEM_TYPE: [(PENDULUMS, MIN), (LIQUIDS, MIN)]

    },
    "تابع الزمني مطال": {
        "type": "",
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "تابع الزمني مطال زواي": {
        "type": "",
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "زواي": {
        "type": "",

    },
    "الزمني": {
        "type": "",
    },
    "تابعه": {
        "type": "",
    },
    "تابع": {
        "type": "",
    },
    "ثوابت الحركة": {
        "type": PHYSICAL_AMOUNT,
        "unit": [],
        "symbols": [],
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "صلابته": {
        "type": ""
    },
    "الحركة": {
        "type": "",
    },
    "ثوابت": {
        "type": "",
    },
    "مطال": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m"],
        "symbols": ["x"],
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "دور": {
        "type": PHYSICAL_AMOUNT,
        "unit": ["s"],
        "symbols": ["t", 't0'],
        PROBLEM_TYPE: [(PENDULUMS, MIN), (LIQUIDS, MIN)]

    },
    "بدء الزمن": {
        "type": PHYSICAL_AMOUNT,
        "unit": ["s"],
        "symbols": ["t"],
        "value": 0,
    },
    "بدء": {
        "type": "",
    },
    "حدد": {
        "type": "",
    },
    "موضع": {
        "type": "",
    },
    "متحرك": {
        "type": "",
    },
    "المتحرك": {
        "type": "",
    },
    "موضع المتحرك": {
        "type": "",
    },
    'موضع المتحرك لحظة بدء الزمن': {
        "type": PHYSICAL_AMOUNT,
        "unit": [],
        "symbols": ['x'],
    },
    "ساكن": {
        "type": "",
    },
    "يتحرك": {
        "type": "",
    },
    "الاتجاه الموجب": {
        "type": "",
    },
    "الاتجاه السالب": {
        "type": "",
    },
    "الاتجاه": {
        "type": "",
    },
    "الموجب": {
        "type": "",
    },
    "السالب": {
        "type": "",
    },
    "انسحابية": {
        "type": "",
    },
    "دزرانية": {
        "type": "",
    },
    "خرطوم": {
        "type": PROBLEM_TYPE,

        PROBLEM_TYPE: [(LIQUIDS, MAX)]

    },
    "مساحة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m^3"],
        "symbols": ["s"]
    },
    "التدفق الحجمي": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m^3.s^-1"],
        "symbols": ["Q'", "Q"],
        PROBLEM_TYPE: [(LIQUIDS, MAX)]

    },
    "التدفق الكتلي": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["kg.s^-1"],
        "symbols": ["Q'", "Q"],
        PROBLEM_TYPE: [(LIQUIDS, MAX)]

    },
    "التدفق": {
        "type": "",
        PROBLEM_TYPE: [(LIQUIDS, MAX)]

    },
    "الحجمي": {
        "type": "",
    },
    "الكتلي": {
        "type": "",
    },
    "الضغط": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["pa"],
        "symbols": []
    },
    "العمل": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["j"],
        "symbols": ["w"]
    },
    "العمل الميكانيكي": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["j"],
        "symbols": [""]
    },
    "الميكانيكي": {
        "type": "",
    },
    "عندئذ": {
        "type": "",
    },
    "عظمى": {
        "type": "",
    },
    "طويلة": {
        "type": "",
    },
    "تسارع": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m.s^-2"],
        "symbols": [""]
    },
    "الاستطالة السكونية": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m"],
        "symbols": ["x"],
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "الاستطالة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m"],
        "symbols": ["x"],
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "السكونية": {
        "type": "",
    },
    "هزات": {
        "type": "",
        PROBLEM_TYPE: [(PENDULUMS, MIN), (LIQUIDS, MIN)]

    },
    "مظال": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m"],
        "symbols": ["x"],
    },
    "الطاقة الحركية": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["j"],
        "symbols": [""]
    },
    "الطاقة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["j"],
        "symbols": [""]
    },
    "الحركية": {
        "type": "",
    },
    "الكامنة": {
        "type": "",
    },
    "الطاقة الكامنة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["j"],
        "symbols": [""]
    },
    "مهمل الكتلة": {
        "type": "",
        "indication": []
    },
    "الاول": {
        "type": "",
        "indication": []
    },
    "الثاني": {
        "type": "",
        "indication": []
    },
    "الثالث": {
        "type": "",
        "indication": []
    },
    "الرابع": {
        "type": "",
        "indication": []
    },
    "الخامس": {
        "type": "",
        "indication": []
    },
    "السادس": {
        "type": "",
        "indication": []
    },
    "السابع": {
        "type": "",
        "indication": []
    },
    "الثامن": {
        "type": "",
        "indication": []
    },
    "التاسع": {
        "type": "",
        "indication": []
    },
    "العاشر": {
        "type": "",
        "indication": []
    },
    "المطلوب": {
        "type": "",
        "indication": []
    },
    "وتر": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(WAVES, MAX)]

    },
    "مزمار": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(WAVES, MAX)]
    },
    "متشابه الطرفين": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(WAVES, MED)]
    },
    "مختلف الطرفين": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(WAVES, MED)]
    },
    "الطرفين": {
        "type": "",
    },
    "مختلف": {
        "type": "",
    },
    "متشابه": {
        "type": "",
    },
    "تواتر": {

        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["Hz"],
        "symbols": ["f"],
        PROBLEM_TYPE: [(WAVES, MIN), (PENDULUMS, MIN)]

    },
    "طول": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m"],
        "symbols": ["l"]
    },
    "ارتفاع": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m"],
        "symbols": ["l", 'h']
    },
    "كتلة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["kg"],
        "symbols": ["m"]

    },
    "كتلته": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["kg"],
        "symbols": ["m"]

    },
    "كثافة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": [],
        "symbols": []

    },
    "درجة حرارة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["c"],
        "symbols": ["t"]
    },
    "درجة": {
        "type": "",
    },
    "حرارة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["c"],
        "symbols": ["t"]
    },
    'قوة': {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["n"],
        "symbols": ["f", "ft"]
    },
    "سرعة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["m.s^-1"],
        "symbols": ["v"]
    },
    "زمن": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["s"],
        "symbols": ["s"]
    },
    "ثابت صلابته": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["n.m^-1"],
        "symbols": ["k"],
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "ثابت صلابة": {
        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["n.m^-1"],
        "symbols": ["k"],
        PROBLEM_TYPE: [(PENDULUMS, MAX)]

    },
    "صلابة": {
        "type": "",
    },
    "ثابت": {
        "type": "",
    },
    "الصوت الاساسي": {
        "type": "",
        PROBLEM_TYPE: [(WAVES, MAX)]

    },
    "الصوت": {
        "type": "",
        PROBLEM_TYPE: [(WAVES, MAX)]

    },
    "الاساسي": {
        "type": "",
    },
    "تواتر الصوت الاساسي": {

        "type": PHYSICAL_AMOUNT,
        "indication": [],
        "unit": ["Hz"],
        "symbols": ["f"],
        PROBLEM_TYPE: [(WAVES, MAX)]
    },
    "التواترات": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(WAVES, MIN), (PENDULUMS, MIN)]
    },
    "مدروجاته": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(WAVES, MAX)]
    },
    "عدد اطوال الموجة": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(WAVES, MAX)]
    },
    "عدد": {
        "type": "",
    },
    "اطول": {
        "type": "",
    },
    "الموجة": {
        "type": "",
        PROBLEM_TYPE: [(WAVES, MAX)]

    },
    "تهتز": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(WAVES, MIN), (PENDULUMS, MIN)]
    },
    "مغزل": {
        "type": PROBLEM_TYPE,
        PROBLEM_TYPE: [(WAVES, MAX)]
    },
    "مواقت": {
        "type": "",
        "value": ""
    },
    "احسب": {
        "type": "",
        "value": ""
    },
    "استنتج": {
        "type": "",
        "value": ""
    },
    "ربع": {
        "type": ""
    },
    "نصف": {
        "type": ""
    },
    "ثلث": {
        "type": ""
    },
    "زاد": {
        "type": ""
    },
    "نقص": {
        "type": ""
    }
}


def get_all_units(keywords):
    keyword_physical_amount = [keyword for keyword in keywords.values() if keyword['type'] == PHYSICAL_AMOUNT]
    return sorted(list(set([unit.lower() for keyword in keyword_physical_amount for unit in keyword['unit']])), key=len,
                  reverse=True)


def get_term_form_keywords(keywords):
    keywords = [keyword for keyword in keywords.keys() if " " in keyword]
    return sorted(keywords, key=lambda x: 1000 * x.count(" ") + len(x), reverse=True)
