import os
from .Database import Database

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Facebook ==============================\n\n")

def showTimelineActions(user):
    clear_screen()

    while True:
        print("What would you like to do?")
        print("1. See my timeline")
        print("2. Like a post")
        print("3. create post")
        print("0. go back")

        opt = int(input("Option: "))

        if opt==0:
            clear_screen()
            break
        elif opt==1:
            # see the timeline
            clear_screen()
            posts = list(user.post_list)
            for friend in user.friend_list:
                for post in friend.post_list:
                    posts.append(post)
            
            posts.sort(key=lambda p: p.timestamp, reverse=True)

            for post in posts:
                post.showPost()
        elif opt==2:
            pass
        elif opt==3:
            # create a post
            content = input("What's in your mind?: ")
            user.createPost(content)
            clear_screen()
        


# Friend methods
def showFriendsActions(user):
    database = Database.getInstance()
    while True:
        clear_screen()
        print("What would you like to do?")
        print("1. Add a friend")
        print("0. Go back")

        opt = int(input("option: "))

        if opt==0:
            clear_screen()
            break
        elif opt==1:
            clear_screen()
            print("Add a friend by selecting their number (0 to not select anyone)")
            
            user_names = []
            users = database.getAll('users')

            for i, name in enumerate(users.keys()):
                if not name == user.name:
                    print("{} | {}".format(i+1, name)) 
                    user_names[i+1] = name

            
            opt = int(input("opt"))

            if opt == 0:
                continue
            
            user.addFriend(database.get('users', user_names[opt]))
        

# Group methods
def showGroupsActions():
    pass

# Profile methods
def showProfileMethods(user):
    
    while True:
        clear_screen()
        print("What would you like to do?")
        print("1. Show my profile")
        print("2. Modify my bio")
        print("0. Go back")
        opt = int(input("Option: "))

        if opt == 0:
            break
        elif opt == 1:
            user.showProfile()
            input("\n\n\n type to continue...")
            
        elif opt == 2:
            print("Type your bio!")
            bio = input()
            user.modifyBio(bio)
        else:
            print("Please enter a valid function")
