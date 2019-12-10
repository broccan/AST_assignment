from datetime import datetime
import Post


class User:
    """
    Class for implementing User

    """

    bio = ''
    freind_list = []
    group_list = []
    post_list = []

    def __init__(self, first_name: str, last_name: str, birthday: str):
        """
        Constructor for the User class

        Parameters
        ----------
        first_name: str
            first name of the user
        last_name: str
            last name of the user
        birthday: str
            birthday of the user, format dd/mm/yyy
        location: str
            current location

        """
        #  self.age = self._get_age(birthday)  Future implementation

        self.full_name = first_name + " " + last_name
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday

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
        self.freind_list.append(user)
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
        

    