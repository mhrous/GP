import copy

from SOLVE.engine import Engine
from SOLVE.rule_list import ALL_RULE


class Node:
    def __init__(self, state, step=None, _new=None):
        self.state = copy.deepcopy(state)
        self.step = step if step else []
        self._new = _new if _new else []
        self.children = []
        self.parser()

    def add_child(self, child):
        new_state = child['state'] + copy.deepcopy(self.state)
        new_node = Node(new_state, child["step"], child["new"])
        self.children.append(new_node)
        return new_node

    def get_new(self):
        return self._new

    def parser(self):
        new_engine = Engine(ALL_RULE, self.state)
        run = new_engine.run()
        for item in run:
            self.add_child(item)

