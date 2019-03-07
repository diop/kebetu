import re 

def tokenize(text):
    no_punc_text = remove_punctuation(text)
    tokens = split_on_whitespace(no_punc_text)
    return tokens

def split_on_whitespace(text):
    return re.split('\s+', text)

def remove_punctuation(text):
    no_punc_text = re.sub('[,.()]', '', text)
    no_punc_text = re.sub('--', ' ', no_punc_text)
    return no_punc_text     

if __name__ == '__main__':
    import sys 
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokens = tokenize(source)
        print(tokens)
    else:
        print('No source text filename give as argument')