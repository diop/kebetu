# Code Attribution: https://github.com/dmcg89/Tweet-Generator/blob/master/sample.py
import random 

sample_text = 'one fish two fish red fish blue fish'
word_list = sample_text.split()

def histogram(word_list):
    new_dict = {}
    for word in word_list:
        if word not in new_dict:
            new_dict[word] = 1
        else:
            new_dict[word] += 1
    return new_dict

hist = histogram(word_list)

def weighted_random_selection(dico):
    choice = random.randint(1, sum(dico.values()))
    weights_sum = 0

    for key in dico:
        weights_sum += dico[key]
        if choice <= weights_sum:
            return key
            break

def frequency_test(hist, word_list):
    temp_word_list = []
    for i in range(10000):
        selected_word = weighted_random_selection(hist)
        temp_word_list.append(selected_word)
        frequency_list = histogram(temp_word_list)
        for key in frequency_list:
            frequency_list[key] = frequency_list[key]/len(temp_word_list)

        print(frequency_list)

# frequency_test(hist, word_list)
weighted_random_selection(hist)