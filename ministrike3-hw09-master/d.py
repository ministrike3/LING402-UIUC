#!/usr/bin/python3
#Implement the body of d.py so that it produces 
#the same output as that found in d.expected_output

#The program should load the list of file IDs from the NLTK UDHR corpus. 
#The program should iterate through the list of file IDs, 
#keeping track of how many file IDs have been processed so far.

#For each file ID, the program should print out a formatted 
#three digit number (with leading zeroes, if needed) 
#that represents how many file IDs have been examined so far, 
#followed by a space, followed by the file ID.
import nltk
files_list=nltk.corpus.udhr.fileids()
for i in files_list:
  number=files_list.index(i)
  print('{:0<3} {}'.format(str(number+1),i))
