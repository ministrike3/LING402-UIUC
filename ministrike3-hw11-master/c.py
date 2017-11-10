#!/usr/bin/python3

# PART C (10%)
#
# Yupik has voiced and voiceless nasals and fricatives.
#
# Certain Yupik fricatives and nasals are "doubleable";
#    that is, they exist in voiced/voiceless pairs
#    where the voiced/voiceless distinction is denoted graphemically through "doubling":
#
# l   -> ll
# r   -> rr
# g   -> gg
# gh  -> ghh
# ghw -> ghhw
# n   -> nn
# m   -> mm
# ng  -> ngng
# ngw -> ngngw
#
#
# The remaining Yupik consonants do not show this doubling pattern.
#
# For each tokenized word, apply the following automatic devoicing rules:
#
# 1a) If an undoubled (but doubleable) fricative occurs immediately before OR after an unvoiced consonant
#     (where that other consonant is not doubleable),
#     the grapheme for the doubleable voiced fricative is replaced with its voiceless counterpart.
#
# 2) If an undoubled (but doubleable) nasal occurs immediately after an unvoiced consonant
#     (where that other consonant is not doubleable), 
#     the grapheme for the doubleable voiced nasal is replaced with its voiceless counterpart.
#
# 3a) If an undoubled (but doubleable) nasal or fricative occurs immediately after an unvoiced fricative
#     (where that other consonant is doubled),
#     the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
#
# 3b) If an undoubled (but doubleable) nasal or fricative occurs immediately before the unvoiced fricative ll
#     the grapheme for the doubleable voiced consonant is replaced with its voiceless counterpart.
#
# Implement a function called apply_devoicing that accepts a list of graphemes,
#     and returns a list of graphemes with the above rules applied.
#
# When this file is executed, it should:
#    * accept text from standard input,
#    * lowercase it,
#    * tokenizes it into Yupik graphemes using the tokenize function from d.py (with keep_apostrophes=True), 
#    * apply the devoicing rules by calling your apply_devoicing function, 
#    * and print the corresponding output (formatted as words, not lists of graphemes).
#
# (Note: you must import tokenize from d.py)

import sys


from d import *

def apply_devoicing(graphemes):
    list_of_graphemes = ['i', 'a', 'u', 'e', 'p', 't', 'k', 'kw', 'q', 'qw', 'v', 'l', 'z', 'y', 'r', 'g', 'w', 'gh',
                         'ghw', 'f', 'll', 's', 'rr', 'gg', 'wh', 'ghh', 'ghhw', 'h', 'm', 'n', 'ng', 'ngw', 'mm', 'nn',
                         'ngng', 'ngngw']
    vowels=['i', 'a', 'u', 'e']
    stops=['p', 't', 'k', 'kw', 'q', 'qw']
    voiced_fricatives=['v', 'l', 'z', 'y', 'r', 'g', 'w', 'gh', 'ghw']
    voiceless_fricatives=['f', 'll', 's', 'rr', 'gg', 'wh', 'ghh', 'ghhw', 'h']
    voiced_nasal=['m', 'n', 'ng', 'ngw']
    voiceless_nasal=['mm', 'nn','ngng', 'ngngw']
    doublable_but_undoubled=['l','r','g','gh','ghw','n','m','ng','ngw']
    doubled = ['ll', 'rr', 'gg', 'ghh', 'ghhw', 'nn', 'mm', 'ngng', 'ngngw']
    unvoiced_undoubled_consonants = ['p', 't', 'k', 'kw', 'q', 'qw', 'f', 's', 'wh', 'h']
    unvoiced_doubled_consonants = ['ll', 'rr', 'gg', 'ghh', 'ghhw']


    for i in range(0,len(graphemes)):
        meme=graphemes[i]
        for j in range(0,len(doublable_but_undoubled)):
            if meme==doublable_but_undoubled[j]:
                if meme in voiced_fricatives:
                    if i>0:
                        if graphemes[i-1] in unvoiced_undoubled_consonants:
                            graphemes[i]=doubled[j]
                    if i<(len(graphemes)-1):
                        if graphemes[i+1] in unvoiced_undoubled_consonants:
                            graphemes[i]=doubled[j]

    for i in range(0,len(graphemes)):
        meme=graphemes[i]
        for j in range(0,len(doublable_but_undoubled)):
            if meme==doublable_but_undoubled[j]:
                if meme in voiced_nasal:
                    if i>0:
                        if graphemes[i-1] in unvoiced_undoubled_consonants:
                            graphemes[i]=doubled[j]

    for i in range(0,len(graphemes)):
        meme=graphemes[i]
        for j in range(0,len(doublable_but_undoubled)):
            if meme==doublable_but_undoubled[j]:
                if meme in voiced_fricatives:
                    if i>0:
                        if graphemes[i-1] in unvoiced_doubled_consonants:
                            graphemes[i]=doubled[j]
                if meme in voiced_nasal:
                    if i > 0:
                        if graphemes[i - 1] in unvoiced_doubled_consonants:
                            graphemes[i] = doubled[j]

    for i in range(0,len(graphemes)):
        meme=graphemes[i]
        for j in range(0,len(doublable_but_undoubled)):
            if meme==doublable_but_undoubled[j]:
                if meme in voiced_fricatives:
                    if i<(len(graphemes)-1):
                        if graphemes[i+1]=='ll':
                            graphemes[i]=doubled[j]
                if meme in voiced_nasal:
                    if i<(len(graphemes)-1):
                        if graphemes[i+1]=='ll':
                            graphemes[i]=doubled[j]


    return(graphemes)

    pass


if __name__ == "__main__":
    with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
        puncList = [".", ";", ":", "!", "?", "/", "\\", ",", "#", "@", "$", "&", ")", "(", "\""]
        for line in f:
            words=line.split()
            for word in words:
                for punc in puncList:
                    word=word.replace(punc,'')
                print(''.join(apply_devoicing(tokenize(word.lower(),keep_apostrophes=True))),end='')
                print(' ',end='')
            print('')
