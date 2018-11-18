#! /home/cam/anaconda3/bin/python3
"""
file: fib.py
Cameron Kimber
date: 2018-10-24
Class: CSE107
Assignment:
"""
def fib(x):
    if x == 0:
      return 0
    elif x == 1:
      return 1
    else:
        return (fib(x - 1) + fib(x - 2))
def main():
    n = 7
    print(fib(n))
if __name__ == "__main__":
	main()
