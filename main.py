""" The python file allowing the user to interface with the
    facebook classes.

    Developer:

"""
import os 

from facebook.User import User
from facebook.Group import Group
from facebook.Timeline import Timeline
from facebook.Database import Database
from facebook.Interface import *

if __name__ == '__main__':

    database = Database()

    while True:
        user = None

        print("Welcome to facebook!")
        print("1. Log in")
        print("2. Sign up")
        print("0. exit")

        opt = int(input("Option: "))

        clear_screen()
        if opt == 0:
            exit()

        elif opt == 1:
            user_name = input("Username: ")
            user = database.getUser(user_name)

        elif opt == 2:
            print("Sign up!! (by giving us your information your soul belong to us eternally)")
            name = input("Name: ")
            birthday = input("Birthday: ")
            location = input("Location: ")
            user = User(name, birthday, location)
            database.add("users", user)

        else:
            print("Please enter a valid option")
            continue

        while True and not user == None :
            
            clear_screen()
            print("What would you like see?")
            print("0. log out")
            print("1. my timeline")
            print("2. my friends")
            print("3. my groups")
            print("4. my profile")

            switcher = {
                1: showTimelineActions,
                2: showFriendsActions,
                3: showGroupsActions,
                4: showProfileMethods
            }

            opt = int(input("Option: "))
            
            if opt == 0:
                break
            elif opt > 0 and opt <= 4:
                function = switcher[opt]
                function(user)
            else:
                print("invalid option! please select a valid option")
