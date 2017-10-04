#!python3

from random import random, randint


class Dictogram(dict):

    def __init__(self, iterable=None):
        """Initialize this histogram as a new dict; update with given items"""
        super(Dictogram, self).__init__()
        self.types = 0
        self.tokens = 0
        if iterable:
            self.update(iterable)

    def update(self, iterable):
        """Update this histogram with the items in the given iterable"""
        for item in iterable:
            if self.count(item) == 0:
                self.types += 1
                self[item] = 1
            else:
                self[item] += 1

            self.tokens += 1

    def count(self, item):
        """Return the count of the given item in this histogram, or 0"""
        return self.get(item, 0)

    def get_random_word(self):
        prob = random()
        accumulator = 0.0
        keys = list(self.keys())
        current_key = None

        while accumulator < prob:
            current_key = keys.pop(randint(0, len(keys) - 1))
            next_probability = self[current_key] / self.tokens
            if accumulator + next_probability > prob:
                break
            else:
                accumulator += next_probability
        return current_key
