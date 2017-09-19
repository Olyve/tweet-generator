#!python3

"""Used to print out a specified number of random words from the the system dictionary."""
from random import randint
from sys import argv


def random_sentence(num):
    """Generates and returns a sentence of random words using get_random_word()."""
    sentence = ''
    for _ in range(0, num):
        sentence += (get_random_word() + ' ')
    return sentence


def get_random_word():
    """Returns a random word from the system dictionary."""
    words = get_sys_dictionary()
    return words[randint(0, len(words) - 1)].rstrip('\n')


def get_sys_dictionary():
    """Creates a list of all the words in the system dictionary."""
    dictionary_path = '/usr/share/dict/words'
    return open(dictionary_path).readlines()


# print(random_sentence(8))

if __name__ == '__main__':
    num_of_words = int(argv[1])
    print(random_sentence(num_of_words))
