#! /home/cam/anaconda3/bin/python3
"""
file: luhns.py
Cameron Kimber
date: 2018-10-03
Class: CSE107
Assignment: lab5- Day-to-day Luhn's Algorithm, regular CS freshman stuff.
"""

diners_ex = 38520000023237


def validate(card_number):

    """
    Runs Luhns algorithm on a given number and returns true or false depending
    on the outcome. I know the generator statements are not strictly
    necessary, but this is kinda too easy so I am trying be slick.
    Personally, I think it is working.

    The first generator statement is separating and rejoining each digit in
    the list created by the second and third statements. Statement 2 starts
    at index -2, and doubles the value in each, and appends them to a
    hypothetical list. Statement 3 grabs the leftovers, and  appends them
    to the same hypothetical list.
    """

    if sum([int(i) for i in ''.join(str(i) for i in
           [int(i) * 2 for i in str(card_number)[-2::-2]]
           + [int(i) for i in str(card_number)[-1::-2]])]) % 10 == 0:
        return True

    else:
        return False


def main():

    print(validate(diners_ex))


if __name__ == "__main__":

    main()
