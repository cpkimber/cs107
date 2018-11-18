#! /home/cam/anaconda3/bin/python3
"""
file: palindrome.py
Cameron Kimber
date: 2018-10-31
Class: CSE107
Assignment:
"""


def palindromer(string):

    if len(string) == 0:
        return True
    if string[0] != string[-1]:
        return False
    return palindromer(string[1:-1])


def main():

    string1 = "Not a palindrome"
    string2 = "racecar"
    print(palindromer(string1))
    print(palindromer(string2))


if __name__ == "__main__":
    main()
