import turtle



n = float(input("Gimme an angle plz: "))
m = 50

t1 = turtle.Turtle()
turtle.tracer(False)
for i in range(128):
  t1.forward(m)
  t1.right(n)
  m+=0.6

turtle.update()
turtle.done()
