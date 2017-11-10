#!/usr/bin/python3

from sys import stdin

# Iterate over each line of standard input
for input_line in stdin:
    # Remove leading and trailing whitespace
    line=input_line.strip()
    # Remove leading and trailing parens
    line=line.strip("()")
    # Remove leading and trailing whitespace
    line=line.strip()
    # Print the output_line
    print(line)
