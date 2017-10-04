import cleanup
from histogram_oop import Dictogram
from random import choice
import random

"""
Markov Chain Code Reference to Alex Dejeu's article and sample code from HackerNoon
https://hackernoon.com/from-what-is-a-markov-model-to-here-is-how-markov-models-work-1ac5f4629b71
Refactoring with 1st Order Markov Model using python3.6
# Used Dictorgram class to access my histogram
#1 Used dictionary as data structure to create the markov chain
#2 For every word in the cleaned file - go through and update a historgram for the value
#3 Generate those tokens inside each historgram. 
#4 create the histogram for every single word
#5 set up and the if else statement and acces sets those words to the Dictogram inside our list
"""
def markov_chain(data):
	"""markov model for 1st ordergi"""
    markov_chain = dict()
    for index in range(0, len(data) - 1):
        if data[index] in markov_chain:
            markov_chain[data[index]].update([data[index + 1]])
        else:
            markov_chain[data[index]] = Dictogram([data[index + 1]])
    return markov_chain
 
def get_start_token(markov):
	"""create a random starting word as our token start"""
	return random.choice(list(markov.keys()))

def get_stop_token(markov):
	"""create a stop token for the end of the sentence"""
	pass

def get_random_sentence(length, markov_chain):
	# input variable is the length of the sentence
	# refactor sampling and create a Markov running sentences
	# loop through the dictogram and append the current word to the previous word
	# join the sentences to form a word
	# returns the sentence
    current_word = get_start_token(markov_chain)
    sentence = [current_word]
    for i in range(0, length):
        current_dictogram = markov_chain[current_word]
        #import pdb; pdb.set_trace()
        print ("___________________")
        print (current_dictogram)
        random_word = current_dictogram.return_weighted_random_word()
        current_word = random_word
        print ("___________________")
        print ('my current word: ' + current_word)
        sentence.append(current_word)
    return ' '.join(sentence) + '.'
    return sentence


# testing my codes using pdb
# start_words = get_start_token(cleaned_file)
# testing with Dr. Sessus words 
file_name = '../text/fish.txt'
cleaned_file = cleanup.clean_file(file_name)
markov_chain = markov_chain(cleaned_file)
# testing for 11 words 
print (generate_random_sentence(11, markov_chain))