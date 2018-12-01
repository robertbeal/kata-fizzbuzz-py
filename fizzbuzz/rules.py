from fizzbuzz.rule import Rule

class Rules(list):
    def __init__(self):
        list.__init__(self)
        self.append(Rule((lambda i: i % 3 == 0), 'Fizz'))
        self.append(Rule((lambda i: i % 5 == 0), 'Buzz'))
