
class Rule(object):
    def __init__(self, expression, value):
        self.expression = expression
        self.value = value

    def applies_to(self, input):
        return self.expression(input)
