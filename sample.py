#!python3

from sys import argv
from random import randint


def create_histogram(filename):
    f = open(filename, 'r')
    lines = f.readlines()
    f.close()

    histogram = []
    for line in lines:
        line = line.rstrip('\n').split(' ')
        histogram.append([line[0], int(line[1])])
    return histogram


if __name__ == '__main__':
    arguments = argv[1:]
    histogram = create_histogram(arguments[0])
    output = ""
    for num in range(0, int(arguments[1])):
        rand_idx = randint(0, len(histogram) - 1)
        output += (histogram[rand_idx][0] + ' ')
    print(output)
