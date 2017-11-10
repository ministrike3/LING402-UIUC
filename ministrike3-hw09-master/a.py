#!/usr/bin/python3

#Implement the body of a.py so that it produces the
#same output as that found in a.expected_output

#The program should create a word-for-word translation
#dictionary from Spanish to English using the Swadesh lists from NLTK.

#The program should iterate over each sentence in the "Spanish-Latin1"
#file in the NLTK UDHR corpus. For each word in the Spanish sentence,
#if the word is in the Spanish-to-English translation dictionary,
#print the English translation;
#otherwise print "UNK". Each sentence should be printed on one line.
import nltk

es2en = nltk.corpus.swadesh.entries(['es', 'en'])
translate = dict(es2en)
need_to_be_translate = nltk.corpus.udhr.sents("Spanish-Latin1")

for sentence in need_to_be_translate:
    new = ''
    for word in sentence:
        if word in translate:
            new += translate[word]+' '
        else:
            new += 'UNK'+' '
    print(new)
