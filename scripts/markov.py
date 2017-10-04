#!python3

from sys import argv
import re

from dictogram import Dictogram


class Markov:

    def __init__(self, iterable):
        """Initialize with an empty dictionary of word nodes.

        Iterable should be a list of sentences ready to be parsed into nodes.
        """
        self.nodes = {}
        self.update(iterable)

    def update(self, iterable):
        """Takes a list of lines and processes them into nodes"""
        for sentence in iterable:
            # Cleaning stuff should be removed eventually
            cleaned_sentence = sentence.rstrip('\n')
            cleaned_sentence = re.sub(r'[.!?]*', '', cleaned_sentence)
            words = list(cleaned_sentence.split(' '))
            for index, word in enumerate(words):
                if word == words[0]:
                    self.update_node('[START]', word)
                elif word == words[len(words) - 1]:
                    self.update_node(word, '[END]')
                else:
                    self.update_node(word, words[index + 1])

    def update_node(self, word, next_word):
        if word in self.nodes:
            self.nodes[word].update([next_word])
        else:
            self.nodes[word] = Dictogram([next_word])

    def get_next(self, current_word):
        pass


if __name__ == '__main__':
    filename = argv[1]
    _file = open(filename, 'r')
    lines = _file.readlines()

    markov = Markov(lines)
    for node in markov.nodes:
        print(node)
        print(markov.nodes[node])
