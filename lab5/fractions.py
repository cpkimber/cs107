#! /home/cam/anaconda3/bin/python3
"""
file: fractions.py
Cameron Kimber
date: 2018-10-05
Class: CSE107
Assignment:
  any fraction can be written as the division of two integers.
  express this in python as a tuple.
  write functions to reduce fractions, add 2 fractions, multiply, and divide
  fractions, and return the integer tuple result.
"""
from math import gcd

def reduce(fraction):

    grcd = gcd(fraction[0],fraction[1])
    red_fr = ((int(fraction[0]/grcd), int(fraction[1]/grcd)))
    return [red_fr[0],red_fr[1]]

def add(frac1, frac2):

    new_frac = ((frac1[0] * frac2[1] + frac2[0]*frac1[1]),
                 (frac1[1]*frac2[1]))
    return reduce(new_frac)


def multiply(frac1, frac2):

    return reduce(((frac1[0] * frac2[0]),(frac1[1] * frac2[1])))


def divide(frac1, frac2):

    return reduce((frac1[0] * frac2[1],(frac1[1] * frac2[0])))

def main():

    firstFrac = input("Enter a fraction >>> ")
    seconFrac = input("Enter a fraction >>> ")
    fFrac = tuple([int(i) for i in firstFrac.split("/")])
    sFrac = tuple([int(i) for i in seconFrac.split("/")])

    print("The first fraction reduces to {}. The second reduces to {}".format
          ('/'.join(str(i) for i in reduce(fFrac)),
          ('/'.join(str(i) for i in reduce(sFrac)))))
    print("The sum of the fractions is {}".format
          ('/'.join(str(i) for i in reduce(add(fFrac, sFrac)))))
    print("Their product is {}".format(
          ('/'.join(str(i) for i in reduce(multiply(fFrac, sFrac))))))
    print("Division of the first by the second is {}".format
          ('/'.join(str(i) for i in reduce(divide(fFrac, sFrac)))))

if __name__ == "__main__":
	main()
