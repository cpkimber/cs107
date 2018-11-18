#! /home/cam/anaconda3/bin/python3
"""
file: fact.py
Cameron Kimber
date: 2018-10-24
Class: CSE107
Assignment:
"""
from math import log
e = 2.71828182845904523536028747135266249775724709369995
def factorial(x):
    if x <= 0:
      return 1
    else:
      return factorial(x-1)*x

def stirling(x):
    return ((2 * 3.14159269 * x) * (x / e)**(x))

def main():
    n = eval(input("Enter a number>> "))
    print('%2.2e' % factorial(n))
    print("%2.2e" % stirling(n))
if __name__ == "__main__":
	main()
