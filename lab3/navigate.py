#! /home/cam/anaconda3/bin/python3
"""
file: navigate.py
Cameron Kimber
date: 2018-09-25
Class: CSE107
Assignment: Write a program that takes directions from the command line to
draw a line. Let the user input “left”, “right”, “forward”, or “stop”.
Left and right turn the turtle left or right however many
degrees are entered, forward moves the turtle forward
(however far you wish), and stop ends the program
"""

import turtle

t = turtle.Turtle()


def main():
    while True:

        direction = input("Please enter a direction: ")
        if direction == "forward":
            t.fd(100)
        elif direction == "right" or direction == "left":
            degrees = eval(input("How many degrees? "))
            if degrees <= 0:
                print("Invalid number, not moving.")
            else:
                if direction == "right":
                    t.right(degrees)
                else:
                    t.left(degrees)
        elif direction == "stop":
            break


if __name__ == "__main__":
    main()
