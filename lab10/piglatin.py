#! /home/cam/anaconda3/bin/python3
"""
file: piglatin.py
Cameron Kimber
date: 2018-11-17
Class: CSE107
Assignment:
"""


def pigger(piggingText, outputFile):

    vowels = "aeiouAEIOU"
    pigList = []
    punc = [".", "?", "'", ",", "!", "-", "(", ")", ";", ":"]
    for word in piggingText.split():
        counter = 0
        for thing in punc:
            if thing in word:
                word = "".join(word.split(thing))
        for letter in word:
            if letter not in vowels:
                counter += 1
            else:
                break
        if counter != 0:
            pigWord = word[counter:] + word[0:counter] + "ay"
            pigList.append(pigWord)
        else:
            pigWord = word + 'way'
            pigList.append(pigWord)
    pigString = " ".join(pigList)
    with open(outputFile, 'w') as outputText: outputText.write(pigString)


def textGrabber(inputFile):

    with open(inputFile, 'r') as inputText:
        text = inputText.read()
        return text

def main():

    piggingTarget = textGrabber("alice.txt")
    pigger(piggingTarget, "alicepig.txt")


if __name__ == "__main__":

    main()
