#! python3

''' 
program that translates english phrases into pig latin

'''

def create_pig_latin(word):
    '''
    function used to check each word in a phrase and
    translate it into pig latin
    '''
    # if word begins with consonant
    if word[0] not in ['a', 'e', 'i', 'o', 'u']:
        # move first letter to end of word, add 'ay' to end
        cons_word = word[1:] + word[0] + 'ay'
        return cons_word
    else:  
    # if word begins with vowel add 'way' to end of word
        vowel_word = word + 'way'
        return vowel_word

if __name__ == '__main__':
    # user input
    phrase = input('Enter a phrase in English: ')
    # for each word in phrase, translate word using
    # create_pig_latin function
    print(' '.join(create_pig_latin(word) for word in phrase.split()))