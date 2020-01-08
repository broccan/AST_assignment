import os

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')
    print("Facebook ==============================\n\n")

def showTimelineActions(user):
    clear_screen()
    #timeline = Timeline()
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
            
            users = {}

            for i, name in enumerate(database['users'].keys()):
                if not name == user.name:
                    print("{} | {}".format(i+1, name)) 
                    users[i+1] = name

            
            opt = int(input("opt"))

            if opt == 0:
                continue
            
            user.addFriend(database['users'][users[opt]])
        

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
