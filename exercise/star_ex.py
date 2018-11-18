import turtle
import random

t1 = turtle.Turtle()

for k in range(10):
    t1.penup()
    t1.setposition(random.randint(-300, 300), random.randint(-300, 300))
    t1.pendown()
    n = random.randint(30, 100)

    for i in range(5):
        t1.forward(n)
        t1.right(144)

turtle.exitonclick()
