import os
import sys

import cleanup
import tokenized
import word_count
import sample
from sentence import markov_dictograms, markov_chain 

from flask import Flask
from flask import render_template 

app = Flask(__name__, template_folder='templates', static_folder='static')

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(ROOT_DIR + '/corpus.txt', 'r') as f:
    corpus = f.read().replace('\n', ' ')

@app.route('/')
def main():
    proverbs_dict = markov_dictograms(corpus)
    sentence = markov_chain(proverbs_dict)
    return render_template('index.html', sentence=sentence)

if __name__ == '__main__':
    app.run()