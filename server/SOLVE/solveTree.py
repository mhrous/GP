from SOLVE.specialTree import handle_special

import json

from SOLVE.node import Node
from SOLVE.specialTree import handle_special


class SolveTree:
    def __init__(self, data):
        state = data["state"]
        keyword = data["keyword"]
        line = data["line"]
        non_used_keywords = data["non_used_keywords"]
        symbols = data["symbols"]
        type_ = data["type"]

        self.head = Node(state)

        self.init(data)

    def init(self, data):
        special = handle_special(data)
        for item in special:
            self.head.add_child(item)

    def parser(self):
        result = {}
        array = [self.head]
        visited = set()
        while len(array):
            first = array[0]
            array = array[1:] + first.children
            for _new in first.get_new():
                json_str = json.dumps({_new: first.step})
                if json_str in visited:
                    continue
                else :
                    visited.add(json_str)
                if _new in result:
                    result[_new].append(first.step)
                else:
                    result[_new] = [first.step]

        return result
