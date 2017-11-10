#!/usr/bin/python3

#Implement the body of c.py so that it produces the 
#same output as that found in c.expected_output

#The program should load the list of file IDs from the NLTK UDHR corpus. 
#For each file ID, the program should print the file ID, followed by a space, 
#followed by the number of words in that file, 
#followed by a space, followed by the number of unique words in that file.

import nltk

files_list = nltk.corpus.udhr.fileids()

for i in files_list:
    words=nltk.corpus.udhr.words(i)
    uniq=set(words)
    print('{} {} {}'.format(i,str(len(words)),str(len(uniq))))
