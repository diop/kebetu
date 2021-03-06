
# Code attribution: https://github.com/anselb/Tweet-Generator/blob/master/source/markov.py 
from dictogram import Dictogram
import sample
from random import randint

def markov_dictograms(text):
    arr = text.split()
    dico = {}

    for word_index in range(len(arr) - 1):
        current_word = arr[word_index]
        next_word = arr[word_index + 1]

        if current_word in dico:
            dico[current_word].add_count(next_word)
        else:
            dico[current_word] = Dictogram([next_word])
    return(dico)

def markov_sample(dictogram):
    return sample.weighted_random_selection(dictogram)

def markov_chain(dictogram_dictionary):
    dictionary_keys = [key for key, value in dictogram_dictionary.items()]
    sentence_array = [dictionary_keys[randint(0, len(dictionary_keys)- 1)]]

    for word_index in range(10):
        word_dictogram = dictogram_dictionary[sentence_array[word_index]]
        next_word = markov_sample(word_dictogram)
        sentence_array.append(next_word)

    return ' '.join(sentence_array)

def nth_order_markov(text, order):
    arr = text.split()
    dico = {}

    for word_index in range(len(arr) - order):
        current_tuple = tuple((arr[index]) for index in range(word_index, word_index + order))
        next_word = arr[word_index + order]

        if current_tuple in dico:
            dico[current_tuple].add_count(next_word)
        else:
            dico[current_tuple] = Dictogram([next_word])
    return dico

def nth_markov_chain(dico):
    dico_keys = [key for key, value in dico.items()]
    sentence_arr = list(dico[randint(9, len(dico) - 1)])

    order = len(sentence_arr)

    for word_index in range(10):
        tuple_key = tuple((sentence_arr[indec]) for index in range(word_index + order))
        if tuple_key in dico:
            dicto_word = dico[tuple_key]
            net_word = markov_sample(dico_word)
            sentence_arr.append(next_word)
        else:
            break
    return ' '.join(setence_arr)

if __name__ == '__main__':
    # fish_text = 'one fish two fish red fish blue fish'

    # fish_markov_dictionary = markov_dictograms(fish_text)
    # print(markov_chain(fish_markov_dictionary))

    with open('corpus.txt', 'r') as f:
        corpus = f.read().replace('\n', ' ')
    # proverb_dict = markov_dictograms(corpus)
    # print(markov_chain(proverb_dict))
    proverb_dict = nth_markov_order(corpus, 2)
    print(nth_markov_chain(proverb_dict))