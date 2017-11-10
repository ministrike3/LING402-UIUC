#!/usr/bin/python3
import myrandom

def main():
    rox = 0
    peper = 0
    scizzors = 0
    for i in range(1, 1000001):
        player = myrandom.rock_paper_scissors()
        if player == 'rock':
            rox += 1
        if player == 'paper':
            peper += 1
        if player == 'scissors':
            scizzors += 1
    print(str(rox)+'\trock')
    print(str(peper)+'\tpaper')
    print(str(scizzors)+'\tscissors')
if __name__ == "__main__":
    main()
