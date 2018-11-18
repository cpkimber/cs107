from math import sqrt, asin, acos, atan

num = float(input("Enter a number to use: "))

ope = input("Which operation? sqrt (s), arcsin (a), arccos (c), arctan (t): ")

if ope == "s":
    if num >= 0:
        print("The square root of the input is",  sqrt(num))
    else:
        print("Invalid input!")

elif ope == "a":
    if -1 <= num <= 1:
        print("The arcsin of the input is", asin(num))
    else:
        print("Invalid input!")

elif ope == 'c':
    if -1 <= num <= 1:
        print("The arccos of the input is", acos(num))
    else:
        print("Invalid input!")

elif ope == 't':
    print("The arctan of the input is", atan(num))

else:
    print("uhh, let's try that one more time")
