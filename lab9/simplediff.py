#! /home/cam/anaconda3/bin/python3
"""
file: simplediff.py
Cameron Kimber
date: 2018-11-07
Class: CSE107
Assignment:
"""


def differ(file1, file2):

    try:
        with open(file1, 'r') as test1:
            lines1 = [line[:-2:] for line in test1]
    except FileNotFoundError:
        print('File {} not found.'.format(file1))
        new_file_1 = input("Please enter the first file name >>> ")
        differ(new_file_1, file2)

    try:
        with open(file2, 'r') as test2:
            lines2 = [line[:-2] for line in test2]
    except FileNotFoundError:
        print("File {} not found.".format(file2))
        new_file_2 = input("Please enter the second file name >>> ")
        differ(file1, new_file_2)

    for i in range(len(lines1)):
        if lines1[i] != lines2[i]:
            for k in range(len(lines2[i])):
                counter = 0
                if lines2[i][k] == lines1[i][k]:
                    counter += 1
            print("{}c{}".format(i + 1, counter))
            print(lines1[i])
            print("---")
            print(lines2[i] + '\n')


def main():

    input_file1 = input("Enter file name 1 >>> ")
    input_file2 = input("Enter file name 2 >>> ")
    differ(input_file1, input_file2)


if __name__ == "__main__":
    main()
