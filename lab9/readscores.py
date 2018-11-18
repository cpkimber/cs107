#! /home/cam/anaconda3/bin/python3
"""
file: readscores.py
Cameron Kimber
date: 2018-11-08
Class: CSE107
Assignment:
"""

def read_scores(lines):

    default_keys = ["state", "act_percent_taking",
                   "act_average_score", "sat_percent_taking",
                   "sat_average_math", "sat_average_reading",
                   "sat_average_writing"]
    data = []
    for line in lines:
        values = line.split()
        row = {}
        for i in range(len(values)):
            row[default_keys[i]] = values[i]
        print(row)
        data.append(row)

def test(input_file):

    data_lines = []
    try:
        with open(input_file, 'r') as datafile:
            for line in datafile:
                data_lines.append(line)
        read_scores(data_lines)

    except FileNotFoundError:
        print("You done typed it in wrong, ya goof!")
        new_file = input("Enter the filename one more time please. >> ")
        test(new_file)


def main():

    test("actsat.txt")


if __name__ == "__main__":
    main()
