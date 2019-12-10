""" The python file allowing the user to interface with the
    facebook classes.

    Developer:

"""
import os 

from facebook.User import User
from facebook.Group import Group
from facebook.Post import Post
from facebook.Timeline import Timeline

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

# Timeline methods
def makePost(user):
    pass

def showTimelineActions(user):

    #timeline = Timeline()
    while True:
        print("What would you like to do?")
        print("1. See my friend's posts")
        print("2. Like a post")
        print("3. Make post")
        print("0. go back")


# Friend methods
def showFriendsActions():
    pass

# Group methods
def showGroupsActions():
    pass

# Profile methods
def showProfileMethods(user):
    clear_screen()
    
    while True:
        print("What would you like to do?")
        print("1. Show my profile")
        print("2. Modify my bio")
        print("0. Go back")
        opt = int(input("Option: "))

        if opt == 0:
            break
        elif opt == 1:
            user.showProfile()
        elif opt == 2:
            print("Type your bio!")
            bio = input()
            user.modifyBio(bio)
        else:
            print("Please enter a valid function")


if __name__ == '__main__':
    print("Welcome to Facebook!")

    database = {
        "users":{},
        "posts":{},
        "groups":{}
    }

    while True:
        user = None

        print("Welcome to facebook!")
        print("1. Log in")
        print("2. Sign up")
        print("0. exit")

        opt = int(input("Option: "))

        if opt == 0:
            exit()

        elif opt == 1:
            user_name = input("Username: ")
            try:
                user = database["users"][user_name]
            except KeyError:
                print("Username not found!")

        elif opt == 2:
            print("Sign up!! (by giving us your information your soul belong to us eternally)")
            name = input("Name: ")
            birthday = input("Birthday: ")
            location = input("Location: ")
            user = User(name, birthday, location)
            database["users"][user.name] = user

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
