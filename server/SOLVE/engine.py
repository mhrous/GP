class Engine:
    def __init__(self, rules=None, state=None):
        self.rules = rules if rules else []
        self.state = state if state else []

    def add_rule(self, new_rule):
        self.rules.append(new_rule)

    def run(self):
        result = []
        for rule in self.rules:
            run = rule.run(self.state)
            if not run:
                continue
            result.append(run)
        return result

    def set_state(self, new_state):
        self.state = new_state


