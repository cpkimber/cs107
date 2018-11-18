import turtle

n = int(input("Please enter positive integer side length: "))

t1 = turtle.Turtle()
t1.penup()
t1.setposition(-4.5 * n, 0)
t1.pendown()

for i in range(3):
    t1.forward(n)
    t1.left(120)

t1.penup()
t1.setposition(-3 * n, 0)
t1.pendown()

for i in range(4):
    t1.forward(n)
    t1.left(360/4)

t1.penup()
t1.setposition(-1.25 * n, 0)
t1.pendown()

for i in range(5):
    t1.forward(n)
    t1.left(360/5)

t1.penup()
t1.setposition(0.85 * n, 0)
t1.pendown()

for i in range(6):
    t1.forward(n)
    t1.left(360/6)

t1.penup()
t1.setposition(3.1 * n, 0)
t1.pendown()

for i in range(7):
    t1.forward(n)
    t1.left(360/7)
