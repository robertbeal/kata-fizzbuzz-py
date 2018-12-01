from fizzbuzz.fizzbuzz import FizzBuzz
from fizzbuzz.rule import Rule
import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_it_says_the_input_if_it_does_not_apply_to_any_rules(self):
        rules = [Rule((lambda i: False), 'foo')]

        self.assertEqual(0, FizzBuzz(rules).say(0))

    def test_it_says_the_rule_value_if_the_input_applies_to_the_rule(self):
        rules = [Rule((lambda i: True), 'foo')]

        self.assertEqual('foo', FizzBuzz(rules).say(0))

    def test_it_applies_multiple_rules(self):
        rules = [
            Rule((lambda i: True), 'foo'),
            Rule((lambda i: True), 'bar')
        ]

        self.assertEqual('foobar', FizzBuzz(rules).say(0))
