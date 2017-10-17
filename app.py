#!python3

from flask import Flask, render_template
from markov import Markov

app = Flask(__name__)


@app.route('/')
def index():
    _file = open('./corpus_cleaned.txt', 'r')
    lines = _file.readlines()
    _file.close()

    markov = Markov(lines)
    min_chars, max_chars = 25, 140
    sentence = markov.generate_sentence()
    while len(sentence) < min_chars or len(sentence) > max_chars:
        # print('sentence too short/long, trying again...')
        sentence = markov.generate_sentence()
    return render_template('index.html', quote=sentence)


if __name__ == "__main__":
    app.run()
