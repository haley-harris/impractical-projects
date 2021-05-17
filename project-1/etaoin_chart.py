#! python3

from collections import defaultdict
from googletrans import Translator
import pprint

'''
program creates a chart showing the number of letters that occur in a
sentence provided by the user - showcasing the most commonly used
letters in english (ETAOIN)

'''

# user input string
text = input('Type a sentence: ')


def translate_to_spanish(text):
    '''
    translates text to spanish
    '''

    # initialize translator instance
    translator = Translator()
    # translate user input text to spanish
    translation = translator.translate(text, dest='es')

    print('\n' + translation.text + '\n')
    return translation.text


def create_bar_graph(text):
    '''
    creates bar graph dictionary
    '''

    ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

    # create dictionary
    mapped = defaultdict(list)

    for c in text:
        # change all chars to lowercase
        c = c.lower()

        if c in ALPHABET:
            mapped[c].append(c)

    # pretty print to have each key/value pair printed on a separate line
    pprint.pprint(mapped)


if __name__ == '__main__':

    create_bar_graph(text)

    # ask if user wants to translate and graph in spanish
    choice = input('Would you like to translate to Spanish? y/n: ').lower()

    if choice == 'y':
        create_bar_graph(translate_to_spanish(text))
