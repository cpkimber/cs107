letter = input("Gimme a single character ")

if 65 <= ord(letter) <= 90 or 97<= ord(letter) <= 122:
  if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or \
  letter == "A" or letter == "E" or letter == "I" or letter == "O" or letter == "U":
    print("That's a vowel homie")
  else: print("That's a consonant my dude")
else:
  print("Hey, that's not even a letter at all!")
