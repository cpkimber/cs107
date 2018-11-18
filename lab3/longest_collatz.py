#! /home/cam/anaconda3/bin/python3
"""
author: Cameron Kimber
date: 2018-09-19
Class:CSE107
Assignment: Lab 3
"""
import collatz


def longest(n):

    l = 0  # stores largest number from sequence
    for i in range(n):
        if collatz.collatz_len(i + 1) > l:
            l = i + 1
    print("The longest chain was %d numbers long, and was %d" %
          (collatz.collatz_len(l), l))


def main():

    print(longest(1000000))


if __name__ == "__main__":
    main()
