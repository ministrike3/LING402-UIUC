#!/usr/bin/python3

#Implement the body of b.py so that it produces 
#the same output as that found in b.expected_output

#The program should load the list of file IDs from the NLTK Gutenberg corpus. 
#For each file ID, the program should print the file ID, followed by a space, 
#followed by the average number of words per line in that file.

import nltk

files_list = nltk.corpus.gutenberg.fileids()

for i in files_list:
    average=len(nltk.corpus.gutenberg.words(i))/len(nltk.corpus.gutenberg.sents(i))
    print('{} {}'.format(i,average))
