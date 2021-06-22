#! python3

import load_dictionary

# load dictionary as list
word_list = load_dictionary.load('words.txt')

# find word pair palingrams
def find_palingrams():

    # palingram list
    pali_list = []

    # create set for time optimization
    words = set(word_list)

# loop through words in list
    for word in words:
        end = len(word)
        rev_word = word[::-1]

        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
                
    return pali_list

palingrams = find_palingrams()

# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

print(f'\nNumber of palingrams: {len(palingrams_sorted)}')

for first, second in palingrams_sorted:
    print(f'{first} {second}')


