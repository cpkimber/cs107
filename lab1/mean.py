print("Please enter 10 numbers, each separated by pressing the <ENTER> key.")

n     = 1
count = 0

while n < 11:
  count += float(input("> "))
  print(count/n)
  n+=1
