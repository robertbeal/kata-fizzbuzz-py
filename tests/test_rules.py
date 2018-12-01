from fizzbuzz.rules import Rules
import unittest

class TestRules(unittest.TestCase):
    def test_it_says_fizz_for_multiples_of_3(self):
        rules = Rules()

        for i in range(1, 100):
            value = i*3
            rule = [rule for rule in rules if rule.applies_to(value)]
            self.assertTrue(rule, "No rule to say 'Fizz' for %s" % value)

    def test_it_says_buzz_for_multiples_of_5(self):
        rules = Rules()

        for i in range(1, 100):
            value = i*5
            rule = [rule for rule in rules if rule.applies_to(value)]
            self.assertTrue(rule, "No rule to say 'Buzz' for %s" % value)
