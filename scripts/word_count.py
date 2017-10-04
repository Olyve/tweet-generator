#!python3

"""Generates a histogram of word count and outputs the results in a text file."""
from sys import argv


def create_histogram(text):
    histogram = {}
    for word in text.split(' '):
        word = word.lower().strip()
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def write_data_to_file(graph, directory):
    data_file = open(directory + 'graph_data.txt', 'w')
    for key in sorted(graph.keys()):
        data_file.write(key + " " + str(graph[key]) + '\n')
    data_file.close()


def unique_words(histogram):
    return len(histogram)


if __name__ == '__main__':
    clean_source = argv[1]
    destination = argv[2]

    source_file = open(clean_source, 'r')
    source_text = source_file.read()
    source_file.close()

    histogram = create_histogram(source_text)
    write_data_to_file(histogram, destination)
