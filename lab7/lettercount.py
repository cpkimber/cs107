#! /home/cam/anaconda3/bin/python3
"""
file: lettercount.py
Cameron Kimber
date: 2018-10-17
Class: CSE107
Assignment:
"""

alphabet_soup = {
                 'a': [1, 0], 'b': [2, 0], 'c': [3, 0], 'd': [4, 0],
                 'e': [5, 0], 'f': [6, 0], 'g': [7, 0], 'h': [8, 0],
                 'i': [9, 0], 'j': [10, 0], 'k': [11, 0], 'l': [12, 0],
                 'm': [13, 0], 'n': [14, 0], 'o': [15, 0], 'p': [16, 0],
                 'q': [17, 0], 'r': [18, 0], 's': [19, 0], 't': [20, 0],
                 'u': [21, 0], 'v': [22, 0], 'w': [23, 0], 'x': [24, 0],
                 'y': [25, 0], 'z': [26, 0]
                 }


def count_letters(string):

    string = string.lower()
    string_list = list(string)

    for i in string_list:
        if i == " ":
            string_list.remove(i)

    for letter in string_list:
        alphabet_soup.get(letter)[1] += 1

    for key in alphabet_soup.items():
        print(key[0], key[1][1] )

def main():

    sample_string = input("Enter some letters >>> ")
    count_letters(sample_string)

if __name__ == "__main__":
	main()
