#!python3

from sys import argv


def remove_chars(text):
    chars_to_remove = [',', '.', ':', '_', ';', '!', '?', '"', '*', '(', ')']
    for char in chars_to_remove:
        text = text.replace(char, '')


def replace_with_space(text):
    chars_to_replace = ['\n', '--']
    for char in chars_to_replace:
        text = text.replace(char, ' ')


# argv - 1: file to edit
if __name__ == '__main__':
    args = argv[1:]
    source = open(args[0], 'r').read()

    remove_chars(source)
    replace_with_space(source)

    test_file = open('./test.txt', 'w')
    test_file.write(source)
    test_file.close()
