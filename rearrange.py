#!python3

import random
from sys import argv


# Returns a random index from the list.
def get_random_index(list):
    return random.randint(0, len(list) - 1)


# Returns a new list that contains the scrambled values of the original list.
def scramble_list(original):
    scrambled = original[::1]
    for _ in range(len(scrambled)):
        first = get_random_index(scrambled)
        second = get_random_index(scrambled)
        scrambled[first], scrambled[second] = scrambled[second], scrambled[first]
    return scrambled


# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# print('original: ', colors)
# print('scrambled:', scramble_list(colors))


if __name__ == '__main__':
    words = argv[1::]
    # print(scramble_list(words))
