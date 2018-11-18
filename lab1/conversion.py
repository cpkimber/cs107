meters_to_feet  = 3.281
meters_to_yards = 1.094
meters_to_miles = 0.0006214

conv_inp = input("Please type a measurement in meters: ")
conv_inp = float(conv_inp)

print("The measurement in feet is:")
print(conv_inp * meters_to_feet)

print("The measurement in yards is:")
print(conv_inp * meters_to_yards)

print("The measurement in miles is:")
print(conv_inp * meters_to_miles)
