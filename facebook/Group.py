class Group:
    """
    Class for implementing Groups

    """

    def __init__(self, name, admin):
        """
        Constructor for the Group class

        Parameters
        ----------
        group_name: str
            name of the group
        admin: User
            User that creates the group
        """

        self.name = name
        self.admin = admin
        self.posts = list()
        self.users = list()

    def deleteGroup(self):
        pass
    
    def addPost(self, new_post):
        """
        Method for add a new post to the group


        Parameters
        ---------
        new_post: Post
            Post posted in the group

        Returns
        -------
        Bool
            True if the new post was successfully added 
            False otherwise
        """
        self.posts.append(new_post)
        return True

    def addUser(self, new_user):
        """
        Method for add a new user to the group


        Parameters
        ---------
        new_user: User
            User added to the group

        Returns
        -------
        Bool
            True if the new user was successfully added 
            False otherwise
        """
        self.users.append(new_user)
        return True

    def removePost(self, post):
        """
        Method to remove a Post from the group


        Parameters
        ---------
        post: Post
            post to be removed

        Returns
        -------
        Bool
            True if the post was successfully removed 
            False otherwise
        """
        try:
            self.posts.remove(post)
            return True
        except:
            return False

    def removeUser(self, admin, member):
        """
        Method to remove a User from the group


        Parameters
        ---------
        user: User
            user to be removed

        Returns
        -------
        Bool
            True if the user was successfully removed 
            False otherwise
        """
        if(admin == self.admin):
            try:
                self.users.remove(user)
                return True
            except:
                return False