import random
import cleanup
import tokenize 
import word_count
import sample
import sentence

from flask import Flask
app = Flask(__name__)

proverbs = ('Only a fool tests the depth of a river with both feet',
         'Knowledge is like a garden: It it is not cultivated, it cannot be harvested',
         'Sugar cane is sweetest at its joints',
          'The best way to eat an elephant in your path is to cut him up into little pieces',
          'A restless foot may walk into a snake pit',
          'A chick that will grow into a cock can be spotted the very day it hatches.',
          'After a foolish deed comes remorse',
          'A roaring lion kills no game',
          'If a child washes his hands he could eat with kings',
          'Rain does not fall on one roof alone',
          'Life is like a shadow and a mist; it passes quickly by, and is no more',
          'Do not look where you fell, but where you slipped'
         )

@app.route('/')
def random_african_proverb():
    rand_index = random.randint(0, len(proverbs) - 1)
    return proverbs[rand_index]
#def hello_world():
    #return 'Only a fool tests the depth of a river with both feet'

if __name__ == '__main__':
    proverb = random_african_proverb()
    print(proverb)
