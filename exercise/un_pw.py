users = {"Cam":"alligator", "Josh":"friday"}


def un_pw():
    user_name = input("What is your name? ")
    password  = input("What is the password? ")

    if user_name in users and users[user_name] == password:
        print("Access Granted")
    elif user_name in users and users[user_name] != password:
        print("Wrong password")
    else:
        print("I don't know you")
