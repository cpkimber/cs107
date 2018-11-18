#! /home/cam/anaconda3/bin/python3
"""
file: markov.py
Cameron Kimber
date: 2018-11-14
Class: CSE107
Assignment:
"""

import random


def markov(input_file):

    word_dict = {}
    with open(input_file, 'r') as text:
        for line in text:
            word_list = line.split()
            for word in word_list[:-1]:
                if word not in word_dict:
                    word_index = word_list.index(word)
                    word_dict[word] = []
                    word_dict[word].append(word_list[word_index + 1])
                else:
                    word_index = word_list.index(word)
                    word_dict[word].append(word_list[word_index + 1])

    return word_dict


def scrambler(dictionary, word):
    generatedChain = ['The']
    new_word = random.choice(dictionary[word])
    print(new_word)
    generatedChain.append(new_word)
    if new_word[-1] != '.':
        scrambler(dictionary, new_word)

def main():

    target_file = input("Input a file to markov >> ")
    try:
        target = markov(target_file)
        print("The")
        scrambler_seed = scrambler(target, 'The')
        scrambler_seed
    except FileNotFoundError:
        target_file = input("Bad file, try again >> ")
        target = markov(target_file)
        print("The")
        scrambler_seed = scrambler(target, "The")
        scrambler_seed
    #(' ').join(generatedChain)

if __name__ == "__main__":
    main()
