#!python3

from sys import argv

phrase = "one fish two fish red fish blue fish"


def create_histogram(text):
    histogram = {}
    for word in text.split(' '):
        word = word.lower()
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram


def unique_words(histogram):
    return len(histogram)


def frequency(word, histogram):
    if word in histogram:
        return histogram[word]
    else:
        return 0


# test_hist = create_histogram(phrase)
# print(test_hist)
# print(unique_words(test_hist))
# print(frequency('fish', test_hist))
# print(frequency('human', test_hist))

if __name__ == '__main__':
    filename = argv[1]
    source = open(filename, 'r').read()

    graph = create_histogram(source)
    output_file = open('./histogram_data.txt', 'w')
    for key in sorted(graph.keys()):
        output_file.write(key + " " + str(graph[key]) + '\n')
    output_file.close()

    print(unique_words(source))
