#!/usr/bin/python3

# PART D (65%)
#
# Define a function called tokenize that accepts a lowercased Yupik word,
# and tokenizes it into Yupik graphemes.
#
# Punctuation within words (apostrophes, etc) is used to separate distinct graphemes
# when they would otherwise be confusable.
#
# For example, "n" followed by "g" would be indicated "n'g" to prevent confusion with "ng"
#
# If the word contains such an apostrophe, then you should use the keep_apostrophes parameter.
# If this parameter is set to True, then you should include the apostrophe in the list of graphemes.
# Otherwise, you should not include the apostrophe in the list of graphemes
#
# Sometimes, your function may be passed an English loan word.
# Such a word is likely to contain alphabetic characters that are not in the Yupik alphabet.
# If a word contains any alphabetic characters that are not in the Yupik alphabet,
#    any such character should be tokenized as an individual token.
#
# For example, the sample text contains the word culturemeng
# 
# The result of tokenize("culturemeng") 
#     should be the list ['c', 'u', 'l', 't', 'u', 'r', 'e', 'm', 'e', 'ng']
#
# If the word contains a character that is not alphabetic and is not an apostrophe,
#     you should discard it.
#
# Sometimes, a word could be tokenized multiple ways, but only one of them will be correct.
# You should implement a greedy longest match, starting at the end of the word.
#
# For example:
#
# The result of tokenize("aanghuutuq")
#     should be the list ['a', 'a', 'n', 'gh', 'u', 'u', 't', 'u', 'q']
#
# The result of tokenize("neghneghngwaaq")
#     should be the list ['n', 'e', 'gh', 'n', 'e', 'gh', 'ngw', 'a', 'a', 'q']
#
#
# When this program is run, it should accept text from standard input,
# lowercase it, remove punctuation outside words, and use your function
# to tokenize it into Yupik graphemes (with keep_apostrophes=False).
#
# Punctuation outside words should be disregarded.

# Grapheme	IPA code point(s)
import sys
def tokenize(word, keep_apostrophes=False):
    list_of_graphemes = ['i', 'a', 'u', 'e', 'p', 't', 'k', 'kw', 'q', 'qw', 'v', 'l', 'z', 'y', 'r', 'g', 'w', 'gh',
                         'ghw', 'f', 'll', 's', 'rr', 'gg', 'wh', 'ghh', 'ghhw', 'h', 'm', 'n', 'ng', 'ngw', 'mm', 'nn',
                         'ngng', 'ngngw']
    split=[]
    while word:
        for i in range(len(word)-1,-1,-1):
            x=i-1
            does_bigger_grapheme_exist=False

            for j in range(0,i):
                if word[j:] in list_of_graphemes:
                    does_bigger_grapheme_exist = True
            if i>=0:
                if word[i-1]=='\'':
                    split.insert(0,word[i:])
                    if keep_apostrophes==True:
                        split.insert(0, '\'')
                    word=word[:i-1]
                elif not does_bigger_grapheme_exist:
                    split.insert(0,word[i:])
                    word=word[:i]
            elif x==0:
                if word!='':
                    split.insert(0, word[i:])
                    word=''
    return(split)


if __name__ == "__main__":
    with open(sys.argv[1], 'r') if len(sys.argv) > 1 else sys.stdin as f:
        puncList = [".", ";", ":", "!", "?", "/", "\\", ",", "#", "@", "$", "&", ")", "(", "\""]
        for line in f:
            words=line.split()
            for word in words:
                for punc in puncList:
                    word=word.replace(punc,'')
                print(tokenize(word.lower()),end='')
                print(' ',end='')
            print('')

