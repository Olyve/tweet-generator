#!python3

import re


def just_rick(source):
    opened_source = open(source, 'r')
    all_text = opened_source.readlines()
    opened_source.close()

    new_source = open('./text-samples/corpus_cleaned.txt', 'w')
    for line in all_text:
        if re.match('Ricks*:', line) or re.match('Rick\s([A-z0-9()-]*)([\s0-9]*):', line):
            line = re.sub('Ricks*:', ' ', line)
            line = re.sub('Rick\s([A-z0-9()-]*)([\s0-9]*):', ' ', line)
            line = re.sub('([([])[A-z.\s]*([)\]])', ' ', line)
            line = re.sub('[\",*()?!/]|[.{1,1}]', ' ', line)
            line = re.sub('\n', ' ', line)
            line = re.sub('\s{2,}', ' ', line)
            # line = line.strip()
            new_source.write(line)
    new_source.close()


if __name__ == '__main__':
    just_rick('./text-samples/original_corpus.txt')