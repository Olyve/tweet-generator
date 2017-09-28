#!python3

import requests
from sys import argv


def scrape_pages(filename):
    pages_file = open(filename, 'r')
    pages = pages_file.readlines()
    pages_file.close()

    corpus = open('./text-samples/original_corpus.txt', 'w')

    token = open('./text-samples/environment_vars.txt', 'r').read().rstrip('\n')
    for page in pages:
        response = requests.get('https://api.diffbot.com/v3/article?token={0}&url={1}'.format(token, page))
        corpus.write(response.json()['objects'][0]['text'])
    corpus.close()


if __name__ == "__main__":
    args = argv[1:]

    scrape_pages(args[0])
