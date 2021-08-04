#! python3

from collections import Counter
import load_dictionary
import sys


# load in dictionary
word_list = load_dictionary.load('words.txt')

# accept name from user
user_name = input('Type your name: ').lower()


def find_anagrams(name, word_list):
    # count letters in user_name
    name_letter_map = Counter(name)

    # empty list to hold anagram phrase
    anagram_list = []

    
    for word in word_list:
        # use test to accumulate all letters that fit in 'name'
        test = ''
        # count letters of each word in list
        letter_map = Counter(word.lower())
        for letter in word:
            # check if count in letter_map is the same or less than the count in name
            if letter_map[letter] <= name_letter_map[letter]:
                # if condition is met, add to the test string
                test += letter
        
        if Counter(test) == letter_map:
            # if test and letter_map are equal, add to anagram list
            anagram_list.append(word)

    print(anagram_list, sep='\n')

    print(f'remaining letters {name}')
    print(f'number of remaining letters = {len(name)}')
    print(f'number of remaining (real word) anagrams = {len(anagram_list)}')
       

def process_choice(name):
    # check user choice for validity, return choice and leftover letters
    while True:
        choice = input('\nMake a choice or press Enter to start over or "n" to end: ')

        if choice == '':
            main()
        elif choice == 'n':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        
        left_over_list = list(name)

        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print("won't work! make another choice", file=sys.stderr)
        
    name = ''.join(left_over_list)
    return choice, name


def main():
    '''Help user build anagram phrase from their name'''
    name = ''.join(user_name.split())
    name = name.replace('-', '')

    limit = len(name)
    phrase = ''
    running = True

    while running:
        temp_phrase = phrase.replace(' ', '')
        if len(temp_phrase) < limit:
            print(f'length of anagram phrase = {temp_phrase}')

            find_anagrams(name, word_list)
            print(f'current anagram phrase = ', end=' ')
            print(phrase, file=sys.stderr)

            choice, name = process_choice(name)
            phrase += choice + ' '

        elif len(temp_phrase) == limit:
            print('\n*****Finished*****\n')
            print('Anagram of name =', end=' ')
            print(phrase, file=sys.stderr)

            try_again = input('\n\nTry again? [y/n] ').lower()
            if try_again == 'n':
                running = False
                sys.exit()
            else:
                main()


if __name__ == '__main__':

    main()
       
       
       
       