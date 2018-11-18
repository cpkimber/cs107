#! /home/cam/anaconda3/bin/python3
"""
description: Your run of the mill fizzbuzzer, nothing to see here
file: fizzbuzz.py
Cameron Kimber
date: 2018-09-19
Class: CSE107
Assignment:
"""


def main():

    i = 0

    x = eval(input("Enter a number: "))
    if x < 0:
        print("Hey, that's not a positive number!")
    else:
        while i <= x:
            if i % 3 == 0 and i % 5 == 0:
                print("{} FizzBuzz".format(i))

            elif i % 3 == 0:
                print("{} Fizz".format(i))

            elif i % 5 == 0:
                print("{} Buzz".format(i))

            else:
                print(i)
            i += 1


if __name__ == "__main__":
    main()
