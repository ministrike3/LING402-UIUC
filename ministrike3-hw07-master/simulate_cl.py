#!/usr/bin/python3
import chutes_and_ladders

def main():
    nums=[0,0,0]
    for i in range(1, 1000001):
        movez=chutes_and_ladders.play_chutes_and_ladders(False)
        if i==1:
            nums[0]=movez
            nums[2]=movez
        else:
            if movez<nums[0]:
                nums[0]=movez
            if movez>nums[2]:
                nums[2]=movez
        nums[1]+=movez
    nums[1]=nums[1]/i
    print(str(nums[0])+'\tmin\n'+str(nums[1])+'\tmean\n'+str(nums[2])+'\tmax\n')
if __name__ == "__main__":
    main()
