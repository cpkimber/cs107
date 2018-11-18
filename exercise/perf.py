#! /home/cam/anaconda3/bin/python3
############################
# Cameron Kimber
# 2018-09-19
# Class: 
# Assignment: 
############################

def perfect_number(x):
    # Takes a perfect number and tests it for perfection
    sum = 0
    
    for i in range(round(x/2)):
        if x%(i + 1) == 0:
            sum+=i + 1
    
    if sum == x:
        print("It is a perfect number")
    else:
        print("It is an imperfect number")

def main(): 
    
    perfect_number(eval(input("Enter a number ")))

if __name__ == "__main__":
	main()
