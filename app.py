#!python3

from flask import Flask
from random import randint
import sample

app = Flask(__name__)


@app.route('/')
def index():
    return sample.generate_sentence('./graph_data.txt', randint(6, 15))


if __name__ == "__main__":
    app.run()
