
class FizzBuzz(object):
    def __init__(self, rules):
        self.rules = rules

    def say(self, input):
        output = ''.join([rule.value for rule in self.rules if rule.applies_to(input)])

        if output:
            return output

        return input
