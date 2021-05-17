#! python3

from collections import defaultdict
import pprint

'''
program creates a chart showing the number of letters that occur in a
sentence provided by the user - showcasing the most commonly used
letters in english (ETAOIN)
'''

# user input string
sentence = input('Type a sentence: ')

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

# create dictionary
mapped = defaultdict(list)

for c in sentence:
    # change all chars to lowercase
    c = c.lower()

    if c in ALPHABET:
        mapped[c].append(c)

# pretty print to have each key/value pair printed on a separate line
pprint.pprint(mapped)

