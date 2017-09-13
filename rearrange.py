import random
from sys import argv


# Returns a random index from the list.
def get_random_index(list):
    return random.randint(0, len(list) - 1)


# Returns a new list that contains the scrambled values of the original list.
def scramble_list(list):
    scrambled = list
    for i in range(len(list)):
        first = get_random_index(list)
        second = get_random_index(list)
        scrambled[first], scrambled[second] = scrambled[second], scrambled[first]
    return scrambled


# print(scramble_list(['red', 'green', 'blue', 'yellow', 'orange', 'purple']))

if __name__ == '__main__':
    words = argv[1::]
    print(scramble_list(words))
