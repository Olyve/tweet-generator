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
    quote = markov.generate_sentence()
    return render_template('index.html', quote=quote)


if __name__ == "__main__":
    app.run()
