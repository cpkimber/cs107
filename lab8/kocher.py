import turtle

def koch_line(width, depth = 0):
    if depth <= 0:
        turtle.forward(width)
    else:
        koch_line(width / 3, depth - 1)
        turtle.left(60)

        koch_line(width / 3, depth - 1)
        turtle.right(2 * 60)

        koch_line(width / 3, depth - 1)
        turtle.left(60)

        koch_line(width / 3, depth - 1)

def koch_snowflake(width=100, depth=1):
    for i in range(3):
        koch_line(width, depth)
        turtle.right(180 - 60)

if __name__ == "__main__":
    turtle.speed('fastest')

    koch_snowflake(9000, 7)

    turtle.done()
