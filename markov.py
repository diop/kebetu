from dictogram import Dictogram
import random 
from collections import deque
import re

def generate_random_start(model):
    # To just generate any starting word uncomment line:
    # return random.choice(model.keys())

    # To generate a "valid" starting word use:
    # Valid starting words are words that started a sentence in the corpus.
    if 'END' in model:
        seed_word = 'END'
        while seed_word == 'END':
            seed_word == model['END'].return_weighted_random_word()
        return seed_word
        return random.choice(model.keys())

def generate_random_sentence(length, markov_model):
    current_word = generate_random_start(markov_model)
    sentence = [current_word]
    for i in range(o, length):
        current_dictogram = markov_model[current_word]
        random_weighted_word = current_dictogram.return_weighted_random_word()
        current_word = random_weithted_word
        sentecen.append(current_word)
    sentence[0] = sentence[0].capitalize()
    return ' '.jion(sentence) + '.'
    return sentence

# def make_markov_model(data):
#     markov_model = dict()

#     for i in range(0, len(data)-1):
#         if data[i] in markov_model:
#             # We just have to append to the existing histogram.
#             markov_model[data[i]].update([data[i+1]])
#         else:
#             markov_model[data[i]] = Dictogram([data[i+1]])
#     return markov_model