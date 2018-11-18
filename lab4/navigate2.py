#! /home/cam/anaconda3/bin/python3
"""
file: navigate.py
Cameron Kimber
date: 2018-09-25
Class: CSE107
Assignment:
Modify navigate.py from lab 3 so that, instead of performing each
action as it is entered, the program accepts user input
without drawing anything until the “stop” command is given all
while ignoring invalid inputs. After the user finishes,
the program should run the drawing commands all at once.
"""

import turtle

t = turtle.Turtle()

commands = []


def main():
    while True:

        direction = input("Please enter a direction: ")
        if direction == "forward":
            commands.append([direction, 100])
        elif direction == "right" or direction == "left":
            degrees = eval(input("How many degrees? "))
            if degrees <= 0:
                print("Invalid number, not moving.")
            else:
                commands.append([direction, degrees])
        elif direction == "stop":
            break

    for command in commands:
        if command[0] == 'forward':
            t.fd(command[1])
        elif command[0] == 'right':
            t.right(command[1])
        elif command[0] == 'left':
            t.left(command[1])
        else:
            break
    turtle.done()


if __name__ == "__main__":
    main()
