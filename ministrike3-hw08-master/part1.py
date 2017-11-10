#!/usr/bin/python3
from sys import stdin
# Create a new variable called level, with an inial value of 0
level=0
# Create a new variable called output_line, with an initial value of ""
output_line=""
# Iterate over each line of standard input
for input_line in stdin:
    # Remove leading and trailing whitespace from the input_line
    line=input_line.strip()
    # If the stripped line is not empty
    if len(line)!=0:
        # Insert a space before each opening paren in the line
        line = line.replace("(", " (")
        # Insert a space after each closing paren in the line
        line = line.replace(")", ") ")
        # Increment level for each opening paren
        level=level+line.count('(')
        # Decrement level for each closing paren
        level=level-line.count(')')
        # Append the current line to the output_line
        output_line+=line
        # If we have read the entire tree
        if level==0:
            # Print output_line
            print(output_line)

            # And reset the output_line variable to an empty string
            output_line=""
