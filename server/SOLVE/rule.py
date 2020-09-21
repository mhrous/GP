class Rule:
    def __init__(self, vars=None):
        self.vars = vars if vars else []
        self.function = {}
        self.can_run_fun = None

    def add_function(self, name, fun):
        self.function[name] = fun

    def set_can_run_fun(self, fun):
        self.can_run_fun = fun

    def can_run(self, state):
        state_items = [s for s in state if s['variable'] in self.vars]
        _len = len(self.vars) - len(state_items)
        return None if _len != 1 else state_items

    def run(self, state):
        if not self.can_run_fun or not self.can_run_fun({"vars":self.vars, "state":state}) :
            return None
        state_items = [s for s in state if s['variable'] in self.vars or s['keyword'] in self.vars]
        print(state,state_items,self.vars)

        state_item_vars = [item['variable'] for item in state_items]
        found = [item for item in self.vars if item not in state_item_vars][0]
        return self.function[found](state_items)
