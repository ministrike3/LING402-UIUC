#!/usr/bin/python3

#Implement the body of d.py so that it produces the same output as that
#found in expected_output/d when run on data/hansards1000.tsv
#need to change commit message
#That data file is a parallel text of French and English sentences,
#with one sentence pair per line. Each line consists of the French
#sentence, followed by a tab, followed by the English sentence.

#The program should first ensure that the user has provided exactly
#one command line argument. If not, the program should fail with a
#usage message of the format "Usage:\t{} file", where {} is replaced by
#the name of the program (you may not hard code the name in the string).

#The program should then read the file, and for each line, the
#program should print the English sentence,
#followed by a tab, followed by the French sentence.

import sys

if len(sys.argv) != 2:
    print('Usage:\t{} file'.format(sys.argv[0]))
    sys.exit()

read_file = open(sys.argv[1])

input_text = []

for line in read_file.readlines():
    raw_data = line.rstrip('\n').split('\t')
    split_data = []
    for x in raw_data:
        split_data.append(x.split('\t'))
    input_text.append(split_data)

for i in range(0,len(input_text)):
    english_string = ''.join(input_text[i][1])
    french_string = ''.join(input_text[i][0])
    print(english_string + "\t" + french_string)
