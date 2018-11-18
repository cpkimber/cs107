#! /home/cam/anaconda3/bin/python3
"""
file: word_count.py
Cameron Kimber
date: 2018-11-07
Class: CSE107
Assignment:
"""


def count_words(tfile, tstring):

    try:
        with open(tfile, 'r') as input_file:
            input_text = input_file.read()
            word_count = 0
            word_list = input_text.split()
            for word in word_list:
                if word == tstring:
                    word_count += 1

        print(word_count)
    except FileNotFoundError:
        print("File '{}' not found".format(tfile))
        new_file_name = input("Please enter a filename: ")
        count_words(new_file_name, tstring)


def main():

    file_name = input("Please enter a filename: ")
    target_string = input("Please enter a string to search for: ")
    count_words(file_name, target_string)


if __name__ == "__main__":
    main()

"""
sample text print print print
sample sample sample print print print
are you not entertained
look at all these words you can count
my gosh
it is like a book up in this mother

print print print
wow
i bet you can not guess which word I am going to use
for my word counter
here is a hint
it is print
wow that rhymed
but it won't this time

print

i count 11
"""
