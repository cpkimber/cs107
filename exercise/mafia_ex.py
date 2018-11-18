from random import *

players = ["Cam", "Celia", "Shannen", "Tyjal", "Robert", "Mickael"]

roles = ["v", "v", "v", "w", "v", "w"]

role_list = {}

shuffle(players)

for i in players:
	role_list[i] = roles.pop()

print(role_list)
