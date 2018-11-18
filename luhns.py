#! /home/cam/anaconda3/bin/python3
"""
file: luhns.py
Cameron Kimber
date: 2018-10-03
Class: CSE107
Assignment:
"""

diners_ex = 38520000023237

def validate(card_number):
    """
    Runs Luhns algorithm on a given number and returns true or false
    depending on the outcome.
    I know the generator statements are not strictly necessary, but this is
    kinda too easy so I am trying to make it slick as fuck
    """
    if sum([int(i) for i in ''.join(str(i) for i in \
          [int(i) * 2 for i in str(card_number)[-2::-2]]   \
          + [int(i) for i in str(card_number)[-1::-2]])]) %10 == 0:
        return True
    else:
        return False


def main():

    validate(diners_ex)
if __name__ == "__main__":
	main()
