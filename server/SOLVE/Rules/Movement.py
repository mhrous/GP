from SOLVE.rule import Rule
from sympy import *

speed = Rule(equation={"left": "v", "right": "d/t"})
speed.add_inference({
    "target": "t",
    "steps": [
        {
            "equation": {"left": "t", "right": "d/v"},
            "describe": ""
        }
    ]
})

speed.add_inference({
    "target": "d",
    "steps": [
        {
            "equation": {"left": "d", "right": "v*t"},
            "describe": ""
        }
    ]
})
