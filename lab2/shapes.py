from math import pi

shape = input("Please enter a shape: ")

if shape   == "circle":
    radius = float(input("Please enter the radius of the circle: "))
    print("The circumference of the circle is ")
    print(2 * pi * radius)
    print("The area of the circle is ")
    print(pi * radius ** 2)

elif shape == "square":
    side   = float(input("Please enter the side length of the square: "))
    print("The perimeter of the square is")
    print(4 * side)
    print("The area of the square is")
    print(side * side)

else:
    width  = float(input("Please enter the width of the rectangle:"))
    height = float(input("Please enter the height of the rectangle: "))
    print("The perimeter of the rectangle is ")
    print(2 * width + 2 * height)
    print("The area of the rectangle is ")
    print(width * height)
