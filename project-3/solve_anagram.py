#! python3

import load_dictionary
import sys


def solve_anagram():

    # load dictionary list
    dictionary_list = load_dictionary.load('words.txt')

    # accept word from user & change to lowercase
    user_word = input('Type a word: ').lower()

    # empty list to hold anagrams
    anagram_list = []

    # sort user input word
    user_word_sorted = sorted(user_word)

    # loop through each word in list:
    for word in dictionary_list:
        
        # do not add to anagram list if it matches user word
        if word != user_word:
            # sort each word
            sorted_word = sorted(word)

            # if word sorted is equal to user word sorted:
            if sorted_word == user_word_sorted:
                # append unsorted word to anagram list
                anagram_list.append(word)

    # print anagram list
    # if no matches - try a different word
    if len(anagram_list) == 0:
        print('Try a different word')
        solve_anagram()
    else:
        print(anagram_list)  

    # ask user to play again
    play_again = input('Would you like to play again? [y/n] ').lower()
    if play_again == 'y':
        solve_anagram()
    else:
        sys.exit()

    
if __name__ == '__main__':
    
    solve_anagram()