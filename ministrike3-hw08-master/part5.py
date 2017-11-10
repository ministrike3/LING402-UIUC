#!/usr/bin/python3

from sys import stdin


class Entry:
    def __init__(self,line):
        # Remove leading and trailing whitespace from line
        line=line.strip()

        # Split the line on tabs into count, children, and parent
        count,children,parent=line.split('\t')

        # Store count as an integer in self.count
        self.count=int(count)

        # Store children as a string in self.children
        self.children=children

        # Store parent as a string in self.parent
        self.parent=parent



def print_entries(entries):

    # If the number of entries is greater than zero
    if len(entries)>0:

        # Create a new variable called denominator, with an initial value of 0
        denominator=0

        # Iterate over each entry in entries
        for entry in entries:

            # Increment denominator by the count stored in entry
            denominator+=entry.count

        # Iterate over each entry in entries
        for entry in entries:

            # Calculate a probability by dividing entry.count by denominator
            probability=entry.count/denominator

            # Print an output line, using the format string "{}\t{}\t{}",
            #       where the first slot is the probability
            #       and the second slot is the children string stored in entry
            #       and the third slot is the parent string stored in entry
            print(str(probability)+'\t'+entry.children+'\t'+entry.parent)



# Create a new empty string called children
children=""

# Create a new empty list called entries
entries=[]

# Iterate over each line of standard input
for line in stdin:

    # Using line, create a new Entry called current_entry
    current_entry=Entry(line)

    # If the children string stored in current_entry is different from the children string
    if current_entry.children!=children:
        # Print entries
        print_entries(entries)

        # Set entries to be an empty list
        entries=[]

        # Set children to be the children string stored in the current_entry
        children=current_entry.children

    # Append the current_entry to the entries list
    entries.append(current_entry)

# Print entries
print_entries(entries)
