#!python3

import re
from random import randint
from pprint import pprint

from dictogram import Dictogram


START = '[START]'
END = '[END]'


class Markov:

    def __init__(self, iterable):
        """Initialize with an empty dictionary of word nodes.

        Iterable should be a list of sentences ready to be parsed into nodes.
        """
        self.order = 2
        self.nodes = {}
        self.update(iterable)

    def update(self, iterable):
        """Takes a list of lines and processes them into nodes"""
        for sentence in iterable:
            # Cleaning stuff should be removed eventually
            cleaned_sentence = sentence.rstrip('\n').lower()
            cleaned_sentence = re.sub(r'[.!?]*', '', cleaned_sentence)
            words = list(cleaned_sentence.split(' '))

            if len(words) < 3:
                return

            self.update_node(('[START]',), words[0])  # first word
            self.update_node(('[START]', words[0]), words[1])  # first and second words

            for index, word in enumerate(words):
                # print(index, word)
                if index == 0:
                    self.update_node((word, words[1]), words[2])
                elif index == len(words) - 2:
                    self.update_node((word, words[-1]), '[END]')
                elif index == len(words) - 1:
                    pass  # Not really sure what to do here? Stems from very short sentences.
                else:
                    self.update_node((word, words[index + 1]), words[index + 2])

    def update_node(self, pair, next_word):
        if pair in self.nodes:
            self.nodes[pair].update([next_word])
        else:
            self.nodes[pair] = Dictogram([next_word])

    def get_next(self, previous_word, current_word):
        dictogram = self.nodes.get((previous_word, current_word), None)
        if dictogram is None:
            return '[END]'
        return dictogram.get_random_word()

    def generate_sentence(self):
        words = list()
        # print('words:', words)

        # TODO: Generate first word based on transitions from [START] state
        starters = list(filter(lambda x: x[0] == '[START]', self.nodes.keys()))
        first_word = starters[randint(0, len(starters) - 1)]
        words.append(first_word[1])

        second_word = self.get_next(*first_word)
        words.append(second_word)  # Expand the tuple into both arguments

        while True:
            next_word = self.get_next(words[-2], words[-1])
            if next_word == '[END]':
                break
            words.append(next_word)

        sentence = " ".join(words)
        return sentence


def main():
    from sys import argv
    filename = argv[1]
    _file = open(filename, 'r')
    lines = _file.readlines()

    markov = Markov(lines)

    min_chars, max_chars = 30, 140
    sentence = markov.generate_sentence()
    while len(sentence) < min_chars or len(sentence) > max_chars:
        print('sentence too short/long, trying again...')
        sentence = markov.generate_sentence()
    print(sentence)


if __name__ == '__main__':
    main()
