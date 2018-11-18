#! /home/cam/anaconda3/bin/python3
"""
file: collatz.py
Cameron Kimber
date: 2018-09-26
Class: CSE107
Assignment: Find the collatz length of a given number
"""


def collatz_len(number):
    length = 1
    while number != 1:
        if number % 2 == 0:
            number = number/2
            length += 1
        else:
            number = 3 * number + 1
            length += 1
    return length


def main():

    print(collatz_len(eval(input("Enter a starting number: "))))


if __name__ == "__main__":
    main()
