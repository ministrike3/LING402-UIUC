#!/usr/bin/python3
import myrandom

def move(starting_space,distance):
    new_position = starting_space+distance
    if new_position > 100:
        new_position= starting_space
    positional_changes = [(1,38),(4,14),(9,31),(21,42),(28,84),(36,44),(51,67),(71,91),(80,100),(16,6),(47,26),(49,11),(56,53),(62,19),
    (64,60),(87,24),(93,73),(95,75),(98,78)]
    for movement in positional_changes:
        if new_position == movement[0]:
            new_position = movement[1]
    return(new_position)

def play_chutes_and_ladders(bool_val):
    current_position = 0
    move_count = 0
    while current_position != 100:
        old_position = current_position
        how_far = myrandom.chutes_and_ladders_spinner()
        current_position = move(current_position,how_far)
        move_count += 1
        if bool_val:
            print(str(old_position)+'\t'+str(how_far)+'\t'+str(current_position))
    return(move_count)

if __name__ == "__main__":
    play_chutes_and_ladders(True)
