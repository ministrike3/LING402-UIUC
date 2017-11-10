#!/usr/bin/python3

# PART A (15%)
#
# Yupik syllables must be of the form:
#
# * CV
# * CVC
# * CVV
# * CVVC
#
# Additionally, the first syllable of a word may be of the form:
#
# * V
# * VC
# * VV
# * VVC
#
# Where C represents a Yupik consonant and V represents a Yupik vowel.
#
#
# In all cases, the only instances of VV that are allowed are:
#
# * ii
# * aa
# * uu
#
#
# Yupik words may contain apostrophe (to separate otherwise ambiguous grapheme sequences).
#
#
# You will need to import tokenize from d.py
#
#
# Implement the violates_spelling_rules function.
# The function should take a string representing a word,
#     tokenize it using your tokenize function,
#     and return True if the word violates Yupik spelling rules (contains a non-Yupik grapheme or violates syllable structure),
#     and return False otherwise.
#
#
# When this file is executed, it should:
#     * accept text from standard input
#     * tokenize it into words
#     * check each word to see if it violates Yupik spelling rules (using your function)
#     * and output a list of all words that violate Yupik spelling rules (one word per line)
#
# In other words, this program will function as a basic Yupik spell checker.
#
#
# No sample expected output will be provided for this program, but sample-ocr.txt contains many misspelled words.
import sys
from d import *


def recursive_checker(testing_structure):
    #print('recursive called on ')
    #print(testing_structure)
    cvvc = True
    cvc = True
    cvv = True
    cv = True
    if len(testing_structure) == 0:
    #    print('Testing structure is length 0 this is a legal word')
        return (False)

    if len(testing_structure) >= 4:
        new_syllable = 'CVVC'
        if testing_structure[0:len(new_syllable)] == new_syllable:
            remains_of_word = testing_structure[len(new_syllable):]
            cvvc = recursive_checker(remains_of_word)

    if len(testing_structure) >= 3:
        new_syllable = 'CVC'
        if testing_structure[0:len(new_syllable)] == new_syllable:
            remains_of_word = testing_structure[len(new_syllable):]
            cvc = recursive_checker(remains_of_word)

    if len(testing_structure) >= 3:
        new_syllable = 'CVV'
        if testing_structure[0:len(new_syllable)] == new_syllable:
            remains_of_word = testing_structure[len(new_syllable):]
            cvv = recursive_checker(remains_of_word)

    if len(testing_structure) >= 2:
        new_syllable = 'CV'
        if testing_structure[0:len(new_syllable)] == new_syllable:
            remains_of_word = testing_structure[len(new_syllable):]
            cv = recursive_checker(remains_of_word)

    if cvvc == False:
        return (False)
    if cvv == False:
        return (False)
    if cvc == False:
        return (False)
    if cv == False:
        return (False)

    #print('recursive failed gg')
    return (True)


def violates_spelling_rules(word):
    #print('New Word Starting Here')
    #print(word)
    list_of_graphemes = ['i', 'a', 'u', 'e', 'p', 't', 'k', 'kw', 'q', 'qw', 'v', 'l', 'z', 'y', 'r', 'g', 'w', 'gh',
                         'ghw', 'f', 'll', 's', 'rr', 'gg', 'wh', 'ghh', 'ghhw', 'h', 'm', 'n', 'ng', 'ngw', 'mm', 'nn',
                         'ngng', 'ngngw']
    for meme in word:
        if meme not in list_of_graphemes:
            return (True)

    vowels = ['i', 'a', 'u', 'e']
    current_structure = ''
    first_syllable_form = ['V', 'VC', 'VV', 'VVC', 'CV', 'CVC', 'CVV', 'CVVC']
    # print(word)

    for index in range(0, len(word)):
        meme = word[index]
        if meme in vowels:
            current_structure += 'V'
        else:
            current_structure += 'C'
    is_it_illegal = True
    #print(current_structure)
    for starter_syllable in first_syllable_form:
        if current_structure[0:len(starter_syllable)] == starter_syllable:
            #print('starter syllable accepted')
            #print(starter_syllable)
            remains_of_word = current_structure[len(starter_syllable):]
            #print(remains_of_word)

            if recursive_checker(remains_of_word) == False:
                #print('triggeredFalse')
                is_it_illegal = False
    #print(is_it_illegal)
    return (is_it_illegal)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
        puncList = [".", ";", ":", "!", "?", "/", "\\", ",", "#", "@", "$", "&", ")", "(", "\""]
        for line in f:
            words = line.split()
            for word in words:
                new=word
                for punc in puncList:
                    new = new.replace(punc, '')
                new = tokenize(new.lower(), keep_apostrophes=True)
                if violates_spelling_rules(new):
                    if word[-1] in puncList:
                        word=word[0:-1]
                    print(''.join(word), end='')
                    print(' ', end='')
                    print('')