from datetime import datetime
from .Post import Post


class User:
    """
    Class for implementing User

    """

    def __init__(self, name: str, birthday: str, location: str):
        """
        Constructor for the User class

        Parameters
        ----------
        name: str
            last name of the user
        birthday: str
            birthday of the user, format dd/mm/yyy
        location: str
            current location

        """
        # Sign up values
        self.name = name
        self.birthday = birthday
        self.location = location

        # variables than later get change
        self.bio = ''
        self.friend_list = []
        self.group_list = []
        self.post_list = []

    def modifyBio(self, bio):
        """
        Method for modifying Bio section of profile


        Parameters
        ---------
        bio: str
            new bio for the profile

        Returns
        -------
        Bool
            1 if it successfully modified bio
            0 otherwise
        """
        self.bio = bio
        return True

    def addFriend(self, user):
        """
        Method for adding friend


        Parameters
        ---------
        user: User
            User to add to friend list

        Returns
        -------
        Bool
            1 if it successfully added the user to friend list
            0 otherwise
        """
        self.friend_list.append(user)
        return True

    def joinGroup(self, group):
        """
        Method for joining group


        Parameters
        ---------
        group: Group
            group to join

        Returns
        -------
        Bool
            1 if it successfully added the user to friend list
            0 otherwise
        """
        try:
            group.addUser(self)
            self.group_list.append(group)
        except:
            return False
        return True


    def createPost(self, content):
        """
        Method to add a post

        Parameters
        ----------
        content : str
            The string contents in the post

        Returns
        ----------
            Post
                returns and instance of the post created
        """
        self.post_list.append(Post(self, content))
        return self.post_list[-1]

    def deletePost(self, post):
        """
        Method to remove a post, yet to be implemented

        Parameters
        ----------
        """

    def showProfile(self):
        print("┌───────────── Profile ─────────────┐")
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Location: ", self.location)
        print(" ")
        if not self.bio == '':
            print(self.bio)
        print("└───────────────────────────────────┘")

    