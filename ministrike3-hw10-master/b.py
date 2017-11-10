#!/usr/bin/python3

#Implement the body of b.py so that it produces the same output as
#that found in expected_output/b when run on raw_in/hansards1000.tsv
#need to change commit message
#That raw_in file is a parallel text of French and English sentences,
#with one sentence pair per line. Each line consists of the French
#sentence, followed by a tab, followed by the English sentence.

#The program should first ensure that the user has provided exactly
#one command line argument. If not, the program should fail with a
#usage message of the format "Usage:\t{} file", where {} is replaced
#by the name of the program (you may not hard code the name in the string).

#The program should then read the file.
#The program should tokenize each sentence using nltk.word_tokenize.

#Finally, the program should print the total number of
#unique tokens on the French side of the corpus, followed by a newline,
#followed by the total number of unique tokens on the English side of
#the corpus, followed by a newline.
from nltk.tokenize import word_tokenize
import sys

if len(sys.argv) != 2:
    print('Usage:\t{} file'.format(sys.argv[0]))
    sys.exit()

read_file = open(sys.argv[1])

french = []
english = []

for line in read_file.readlines():
    raw_in = line.strip('\n').split('\t')
    french_token = word_tokenize(str(raw_in[0]))
    french.append(french_token)
    english_token = word_tokenize(str(raw_in[1]))
    english.append(english_token)

french_flatten=[]
for tokens in french:
    for token in tokens:
        french_flatten.append(token)

english_flatten=[]
for tokens in english:
    for token in tokens:
        english_flatten.append(token)

print(len(set(french_flatten)))
print(len(set(english_flatten)))
