class Rule:
    def __init__(self, equation):
        self.equation = equation
        self.inference = []

    def add_inference(self,inf):
        self.inference.push(inf)

    