#!/usr/bin/python3

# PART B (10%)
#
# Implement the graphemes2ipa function.
# It should accept a list of graphemes, and return a list of IPA symbols.
# If any grapheme is not a Yupik letter, it should be passed through unchanged.
#
# When this file is executed, it should:
#     * accepts text from standard input,
#     * lowercases it, 
#     * tokenizes it into Yupik graphemes using your tokenize function from d.py (with keep_apostrophes=False),
#     * applies the automatic devoicing rules using your apply_devoicing function from c.py, 
#     * converts each grapheme into the appropriate IPA symbol using your graphemes2ipa function,
#     * and then print the corresponding output (formatted as words, not lists of graphemes).
#
# You will need to import tokenize from d.py
# You will need to import apply_devoicing from c.py
#
# Your output should not contain any apostrophes.
import sys
from d import *
from c import *

def graphemes2ipa(graphemes):
    list_of_graphemes = ['i', 'a', 'u', 'e', 'p', 't', 'k', 'kw', 'q', 'qw', 'v', 'l', 'z', 'y', 'r', 'g', 'w', 'gh',
                         'ghw', 'f', 'll', 's', 'rr', 'gg', 'wh', 'ghh', 'ghhw', 'h', 'm', 'n', 'ng', 'ngw', 'mm', 'nn',
                         'ngng', 'ngngw']

    list_ipa = ['i', 'ɑ', 'u', 'ə', 'p', 't', 'k', 'kʷ', 'q', 'qʷ', 'v', 'ɮ', 'z', 'j', 'ʐ', 'ɣ', 'ɣʷ', 'ʁ', 'ʁʷ', 'f',
                'ɬ', 's', 'ʂ', 'x', 'xʷ', 'χ', 'χʷ', 'h', 'm', 'n', 'ŋ', 'ŋʷ', 'm̥', 'n̥', 'ŋ̊', 'ŋ̊ʷ']

    for i in range(0,len(graphemes)):
        meme=graphemes[i]
        if meme in list_of_graphemes:
            j=list_of_graphemes.index(meme)
            graphemes[i]=list_ipa[j]
    return(graphemes)



if __name__ == "__main__":
    with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
        puncList = [".", ";", ":", "!", "?", "/", "\\", ",", "#", "@", "$", "&", ")", "(", "\""]
        for line in f:
            words=line.split()
            for word in words:
                for punc in puncList:
                    word=word.replace(punc,'')
                print(''.join(graphemes2ipa(apply_devoicing(tokenize(word.lower())))),end='')
                print(' ',end='')
            print('')