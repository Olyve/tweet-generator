#!python3

import re
from random import randint
from scripts.dictogram import Dictogram

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
            cleaned_sentence = sentence.strip('\n').lower()
            cleaned_sentence = re.sub(r'[.!?]*', '', cleaned_sentence)
            words = list(cleaned_sentence.split(' '))

            if len(words) < 2:
                continue

            self.update_node((START, None), words[0])  # first word
            self.update_node((START, words[0]), words[1])  # first and second words

            queue = [START, words[0], words[1]]

            for index in range(2, len(words)):
                # Shift queue
                queue.append(END) if index == len(words) - 1 else queue.append(words[index])
                queue.pop(0)

                self.update_node((queue[0], queue[1]), queue[2])

    def update_node(self, pair, next_word):
        if pair in self.nodes:
            self.nodes[pair].update([next_word])
        else:
            self.nodes[pair] = Dictogram([next_word])

    def get_next(self, previous_word, current_word):
        dictogram = self.nodes.get((previous_word, current_word), None)
        if dictogram is None:
            return END
        return dictogram.get_random_word()

    def generate_sentence(self):
        words = list()

        first_word = self.get_next(START, None)
        words.append(first_word)

        second_word = self.get_next(START, first_word)
        words.append(second_word)

        while True:
            next_word = self.get_next(words[-2], words[-1])
            if next_word == END:
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

    min_chars, max_chars = 25, 140
    sentence = markov.generate_sentence()
    while len(sentence) < min_chars or len(sentence) > max_chars:
        print('sentence too short/long, trying again...')
        sentence = markov.generate_sentence()
    print(sentence)


if __name__ == '__main__':
    main()
