
import random

def rock_paper_scissors():
    player_moves=['rock','paper','scissors']
    which_one=random.randint(1,3)
    return(player_moves[which_one-1])

def chutes_and_ladders_spinner():
        return(random.randint(1,6))
