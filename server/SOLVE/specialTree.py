import copy
import re

from constants import FUNCTION_AMPLITUDE_FOR_PENDULUMS
from SOLVE.toLetex import py2tex


def handle_function_amplitude_for_pendulums(state):
    obj = copy.deepcopy(state)
    function_amplitude = None
    for item in obj:
        if item['keyword'] == FUNCTION_AMPLITUDE_FOR_PENDULUMS:
            function_amplitude = item["value"]
            break

    if function_amplitude:
        result = {}
        amplitude = "(x(max)?=)?(\d*(\.\d*)?)cos\((.*)t(([+-])(.*)?)\)"
        find = re.search(amplitude, function_amplitude)
        xmax = find.group(3)
        omega = find.group(5)
        operater = find.group(7)
        varphi = find.group(8) if operater == "+" else "-" + find.group(8)

        new_function_amplitude = f"x = {py2tex(xmax)}cos({py2tex(omega)} {operater} {py2tex(varphi)})"
        step = [
            {"type": "text", "value": "لدينا تابع المطال "},
            {"type": "latex", "value": f"$${new_function_amplitude}$$"},
            {"type": "text", "value": ",نحن نعلم ان تابع المطال يكون من الشكل "},
            {"type": "latex", "value": "$$x = x_{max} cos(\omega t + \\varphi )$$"},
            {"type": "text", "value": "بالمقارنة نجد ان"},
            {"type": "latex", "value": "$$ x_{max} = "+py2tex(xmax)+" m ,\omega = "+py2tex(omega)+" rad.s^{-1}, \\varphi = "+py2tex(varphi)+" rad$$"},
        ]
        new_state = [
            {
                "keyword": "سعة اهتزاز",
                "unit": "m",
                "value": xmax,
                "variable": "xmax"
            },
            {
                "keyword": "",
                "unit": "rad.s^-1",
                "value": omega,
                "variable": "omega"
            },
            {
                "keyword": "",
                "unit": "rad",
                "value": varphi,
                "variable": "varphi"
            }
        ]
        result['step'] = step
        result["state"] = new_state
        result["new"] = ["xmax", "varphi", "omega","ثوابت الحركة"]
        return result
    return None


def handle_special(data):
    res = []
    obj = copy.deepcopy(data)
    keyword = obj['keyword']
    line = obj["line"]
    non_used_keywords = obj["non_used_keywords"]
    state = obj["state"]
    symbols = obj['symbols']

    function_amplitude = handle_function_amplitude_for_pendulums(state)
    if function_amplitude:
        res.append(function_amplitude)

    return res
