#!/usr/bin/python3

#Implement the body of a.py so that it produces the same output as that
#found in expected_output/a when run on data/hansards1000.tsv
#need to change commit message
#That data file is a parallel text of French and English sentences,
#with one sentence pair per line. Each line consists of the French
#sentence, followed by a tab, followed by the English sentence.

#The program should first ensure that the user has provided
#exactly one command line argument. If not, the program should
#fail with a usage message of the format "Usage:\t{} file", where {}
#is replaced by the name of the program (you may not hard code the name in the string).

#The program must define a function called pg(word).
# This function must accept a single string as a parameter.
#If the string is more than one character long, and if it contains
#only alphabetic characters, transform the word into its Pig Latin
#equivalent and return that value. Otherwise, return the original string.

#The program should read the file.
# For each line, the program should tokenize
#each sentence using nltk.word_tokenize.
#For each word in the English sentence, convert it to Pig Latin using y
#our pg() function. For each line, print the Pig-Latinized English
#sentence, followed by a tab, followed by the original French sentence.


#Pig Latin
#=========

#For our purposes the set of vowels are a, e, i, o, and u,
#regardless of casing. If y is word-initial it should not
#be treated as a vowel. If y occurs anywhere else in the word,
#treat it as a vowel.

#If a word begins with a vowel, the Pig Latin equivalent is xxxx-ay,
#where xxxx is the original word.

#Otherwise, if the word contains at least one vowel, the Pig
#Latin equivalent is vxxx-zzzzay, where v is the first vowel in the
#word, zzzz is everything before the first vowel, and xxx is
#everything after the first vowel.

#Otherwise if the word contains no vowels, the Pig Latin
#equivalent is xxxxx-ay, where xxxx is the original word.


#from nltk.tokenize import word_tokenize
import sys
import re
from nltk.tokenize import word_tokenize

def pg(string):
    if(len(string) <= 1):
        return string

    elif re.search('[0-9,.``\'-]',string):
        return string

    else:
        lower = string.lower()
        does_a_vowel_exist=False
        vowels = ["a", "e", "i", "o", "u"]
        for i in range(0,len(lower)):
            if lower[i] in vowels:
                does_a_vowel_exist=True
            if i>0:
                if lower[i]=='y':
                    does_a_vowel_exist=True

        if does_a_vowel_exist:
            vowels = ["a", "e", "i", "o", "u"]
            for i in range(0,len(string)):
                if lower[i] in vowels:
                    return string[i:] + '-' + string[:i] + 'ay'
                if i>0:
                    if lower[i]=='y':
                        return string[i:] + '-' + string[:i] + 'ay'

        return string+'-ay'

if len(sys.argv) != 2:
    print('Usage:\t{} file'.format(sys.argv[0]))
    sys.exit()

read_file = open(sys.argv[1])

for line in read_file.readlines():
    english_line=''
    french_line=''
    raw_in = line.strip('\n').split('\t')
    french_tokens  = word_tokenize(str(raw_in[0]))
    english_tokens = word_tokenize(str(raw_in[1]))

    for token in english_tokens:
        piggy=pg(token)
        english_line+=piggy
        english_line+=' '
    for token in french_tokens:
        french_line+=token
        french_line+=' '
    print(english_line+'\t'+french_line)
