gallons = float(input("How many gallons of gas did you burn? "))

if gallons == 0 :
    gallons = float(input("How many gallons of gas did you burn? "))
    print("Whoa there, partner!")
    gallons = float(input("How many gallons of gas did you burn? "))

sum_distance = 0
sum_gas      = 0

while gallons != -1:
  distance = float(input("And how far did that get ya? (-1 to end) "))
  sum_distance += distance
  sum_gas += gallons
  print("Your gas mileage this tank was %2.2f" % (distance/gallons))
  gallons = float(input("How many gallons of gas did you burn? "))

print("Your average fuel economy was %2.2f" %(sum_distance/sum_gas))
