#! python3

import re
from sys import argv
from unidecode import unidecode


def clean_source(filename):
    original_source = open(filename, 'r')
    cleaned_filename = create_cleaned_filename(filename)
    cleaned_source = open(cleaned_filename, 'w')

    remove_unwanted_text(original_source, cleaned_source)
    original_source.close()
    cleaned_source.close()

    return cleaned_filename


def create_cleaned_filename(original_filename):
    file_path = original_filename.split('.txt')
    new_filename = file_path[0] + '_cleaned.txt'
    return new_filename


def remove_unwanted_text(original_file, cleaned_file):
    source_text = original_file.readlines()
    pattern1 = re.compile(r'((All|Doofus|Evil|Council|Pickle)\s)?(Ricks?)\s*([A-z0-9()-]*)([\s0-9]*):')
    pattern2 = re.compile(r'([([])[A-z.\s]*([)\]])')
    pattern3 = re.compile(r'[",]|(\s(-+|\'+)\s)')
    pattern4 = re.compile(r'\.{3}')
    pattern5 = re.compile(r'(?<=[.!?])\s(?=[A-Z*])')
    for line in source_text:
        if re.match(pattern1, line):
            line = unidecode(line)
            line = re.sub(pattern1, ' ', line)
            line = re.sub(pattern2, ' ', line)
            line = re.sub(pattern4, '…', line)
            line = re.sub(pattern3, ' ', line)
            line = line.replace('\n', ' ')
            line = re.sub('\s+', ' ', line)
            line = re.sub(pattern5, '\n', line)
            line = line + '\n'
            line = line.lstrip()
            cleaned_file.write(line)


if __name__ == '__main__':
    source_file = argv[1]
    clean_source(source_file)