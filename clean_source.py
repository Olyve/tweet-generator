#!python3

from sys import argv


def remove_chars(text):
    chars_to_remove = [',', '.', ':', '_', ';', '!', '?', '"', '*', '(', ')']
    for char in chars_to_remove:
        text = text.replace(char, '')
    return text


def replace_with_space(text):
    chars_to_replace = ['\n', '--']
    for char in chars_to_replace:
        text = text.replace(char, ' ')
    return text


# argv - 1: file to edit
if __name__ == '__main__':
    arguments = argv[1:]
    open_file = open(arguments[0], 'r')
    source = open_file.read()
    open_file.close()

    source = replace_with_space(remove_chars(source))

    filename = arguments[0].split('.')[0] + '_cleaned.txt'
    test_file = open(filename, 'w')
    test_file.write(source)
    test_file.close()
