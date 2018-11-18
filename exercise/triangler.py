a = float(input("Gimme a triangle side "))
b = float(input("Gimme a triangle side "))
c = float(input("Gimme a triangle side "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Shit's equilateral, y'all")
    elif a == b or b == c or a ==c:
        print("Shit's isocoles, yo")
    else:
        print("Shit's irreg.")
else:
    print("Shit's not even a triangle")
