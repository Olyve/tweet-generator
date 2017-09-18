#!python3

# This file is used to print out a specified number of random words
# from the the system dictionary.
from random import randint
from sys import argv


def random_sentence(num):
    sentence = ''
    for _ in range(0, num):
        sentence += (get_random_word() + ' ')
    return sentence


def get_random_word():
    words = get_sys_dictionary()
    return remove_trailing_sequence(words[randint(0, len(words) - 1)], '\n')


def remove_trailing_sequence(string, seq):
    return string.rstrip(seq)


def get_sys_dictionary():
    dictionary_path = '/usr/share/dict/words'
    return open(dictionary_path).readlines()


# print(random_sentence(8))

if __name__ == '__main__':
    num_of_words = int(argv[1])
    print(random_sentence(num_of_words))
