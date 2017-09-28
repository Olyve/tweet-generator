#!python3

from random import randint
from flask import Flask, render_template
from scripts import sample

app = Flask(__name__)


@app.route('/')
def index():
    quote = sample.generate_sentence('test_graph_data.txt', randint(6, 20))
    return render_template('index.html', quote=quote)


if __name__ == "__main__":
    app.run()
