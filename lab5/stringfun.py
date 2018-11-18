#! /home/cam/anaconda3/bin/python3
"""
file: stringfun.py
Cameron Kimber
date: 2018-10-03
Class: CSE107
Assignment: Lab 5 stringfun. Does fun stuff with strings, but you
already knew that.
"""


def ends():
    """ Takes a string from the user and returns the first two and
    last two characters of that string"""
    print("== ends ==")
    end_str = str(input("Enter a string >>> "))
    print(end_str[0:2] + end_str[-2:])


def mix():
    """Takes two strings from the user and returns the two strings
    concatenated, but with the first two characters of each swapped.
    Ex: a = german b = english output = geglish enrman"""
    a = str(input("String a >>> "))
    b = str(input("String b >>> "))
    print(b[0:2]+a[2:], a[0:2]+b[2:])


def main():
    ends()
    mix()


if __name__ == "__main__":
    main()
