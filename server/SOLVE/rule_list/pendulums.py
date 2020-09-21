from sympy import *
import re

from SOLVE.rule import Rule

##########################################################################
##################    t0 = 2pi/w #########################################
##########################################################################

t0_omega = Rule(['t0', 'omega'])


def t0_omega_fun_for_t0(state):
    # t0 = 2pi/omega
    result = {}
    omega = [element for element in state if element['variable'] == "omega"][0]
    x = symbols('x', complex=True)
    expr = 2 * pi / x
    omegaValue = x
    value = expr.subs(x, omega['value'])
    step = [
        {"type": "text", "value": "ي البداية نحن نعلم ان  "},
        {"type": "latex", "value": f"$$T_0 = {latex(expr.subs(x, 'omega'))}$$"},
        {"type": "text", "value": "ولدينا "},
        {"type": "latex", "value": f"$$\omega ={latex(omegaValue.subs(x, omega['value']))} $$"},
        {"type": "text", "value": "منه بعض التويض والاختصار  مجد"},
        {"type": "latex", "value": "$$ T_{0} = " + latex(value) + " s"},
    ]
    new_state = [
        {
            "keyword": "دور",
            "unit": "s",
            "value": value,
            "variable": "t0"
        },
    ]
    result['step'] = step
    result["state"] = new_state
    result["new"] = ["t0", 'دور']
    return result


def can_run_for_t0_omega(obj):
    state = obj['state']
    vars = obj['vars']
    state_items = [s for s in state if s['variable'] in vars]
    _len = len(vars) - len(state_items)
    return True if _len == 1 else False


def t0_omega_fun_for_omega(state):
    # omegq = 2pi/to
    result = {}
    t0 = [element for element in state if element['variable'] == "t0"][0]
    x = symbols('x', complex=True)
    expr = 2 * pi / x
    t0Value = x
    value = expr.subs(x, t0['value'])
    step = [
        {"type": "text", "value": "ي البداية نحن نعلم ان  "},
        {"type": "latex", "value": f"$${latex(expr.subs(x, 'T_{0}'))}$$"},
        {"type": "text", "value": "ولدينا "},
        {"type": "latex", "value": f"$$\T_{0} ={latex(t0Value.subs(x, t0['value']))} $$"},
        {"type": "text", "value": "منه بعض التويض والاختصار  مجد"},
        {"type": "latex", "value": "$$ t_{0} = " + latex(value) + " s"},
    ]
    new_state = [
        {
            "keyword": "",
            "unit": "rad.s^-1",
            "value": value,
            "variable": "omega"
        },
    ]
    result['step'] = step
    result["state"] = new_state
    result["new"] = ["omega"]
    return result


t0_omega.add_function('t0', t0_omega_fun_for_t0)

t0_omega.add_function('omega', t0_omega_fun_for_omega)

t0_omega.set_can_run_fun(can_run_for_t0_omega)


# #################################################

def can_run_for_user_position_on_start_time(obj):
    state = obj['state']
    state_items = [s for s in state if s['keyword'] == "تابع المطال للنواس المرن" or s['keyword'] == "موضع المتحرك لحظة بدء الزمن"]

    return len(state_items) == 1


def user_position_on_start_time_fun(state):
    # x = xmax cos(omeq t + vi)
    result = {}
    var_1 = [element for element in state if element['keyword'] == "تابع المطال للنواس المرن"][0]
    amplitude = "(x(max)?=)?(\d*(\.\d*)?)cos\((.*)t(([+-])(.*)?)\)"
    find = re.search(amplitude, var_1['value'])
    xmax = find.group(3)
    value_str = var_1['value'].replace("t","*0").replace(f'{xmax}cos',f'{xmax}*cos')
    value_str2 = var_1['value'].replace("t","*t").replace(f'{xmax}cos',f'{xmax}*cos')

    value =sympify(value_str)
    step = [
        {"type": "text", "value": "دينا تابع المطال للنواس المرن يساوي  "},
        {"type": "latex", "value": f"$${latex(sympify(value_str2))}$$"},
        {"type": "text", "value": "لحظة بدا الزمن اي يجب علينا التويض ب t = 0  "},
        {"type": "text", "value": "منه بعض التويض والاختصار  مجد"},
        {"type": "latex", "value": "$$ x = " + latex(value) + " m"},
    ]
    new_state = [
        {
            "keyword": "موضع المتحرك لحظة بدء الزمن",
            "unit": "m",
            "value": value,
            "variable": "موضع المتحرك لحظة بدء الزمن"
        },
    ]
    result['step'] = step
    result["state"] = new_state
    result["new"] = ["موضع المتحرك لحظة بدء الزمن"]
    print(result)
    return result


user_position_on_start_time = Rule(['تابع المطال للنواس المرن'])
user_position_on_start_time.add_function('تابع المطال للنواس المرن', user_position_on_start_time_fun)

user_position_on_start_time.set_can_run_fun(can_run_for_user_position_on_start_time)

##########################################################################
##################  #########################################
##########################################################################
