import turtle

n_sides = int(input("How many sides? "))

if n_sides < 3:
    print("Invalid input")

else:
    angle   = 360 / n_sides
    length  = float(input("Please enter the side length: "))
    t1 = turtle.Turtle()
    for i in range(n_sides):
        t1.forward(length)
        t1.left(angle)
turtle.done()
