#! /home/cam/anaconda3/bin/python3
"""
file: cesaro.py
Cameron Kimber
date: 2018-11-04
Class: CSE107
Assignment:
"""


import turtle


def cesaro_line(width, depth=0):

    if depth <= 0:
        turtle.forward(width)
    else:
        cesaro_line(width / 2, depth - 1)
        turtle.right(80)

        cesaro_line(width / 2, depth - 1)
        turtle.left(2 * 80)

        cesaro_line(width / 2, depth - 1)
        turtle.right(80)

        cesaro_line(width / 2, depth - 1)


def main():

    turtle.speed('fastest')
    cesaro_line(200, 5)
    turtle.done()


if __name__ == "__main__":
    main()
