import sys
import random

def get_dictionary_words():
    with open('snippet.txt', 'r') as f:
        dictionary_words = f.read().split(' ')
    return dictionary_words

def create_random_sentence(dictionary, num_words):
    for _ in range(num_words):
        random_sentence = ' '.join(random.sample(dictionary, 10)) + '.'
        return random_sentence

def main():
    num_words = int(sys.argv[1])
    dictionary = get_dictionary_words()
    print('words -->', dictionary)
    print(create_random_sentence(dictionary, num_words))

if __name__ == '__main__':
    main()