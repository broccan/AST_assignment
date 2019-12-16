from datetime import datetime

class Post:
    """
    Class for implementing Post

    """
    def __init__(self, owner, content):
        """
        Constructor for the Post class

        Parameters
        ----------
        owner: User
            owner of the post
        content: str
            text contained by the post
        """
        self.owner = owner
        self.content = content
        self.timestamp = datetime.now()
        self.likes = []

    def showPost(self):
        """
        Method to display text contained by a post

        Parameters
        ---------
        None

        Returns
        -------
        None

        """
        print("{} ──────────────────────────".format(self.owner.name))
        print("{:%d, %b %Y}".format(self.timestamp))
        print("{}".format(self.content), end="\n\n")

    def addLike(self, user):
        """
        Method to add users who like the post

        Parameters
        ---------
        user: User

        Returns
        -------
        None

        """
        self.likes.append(user)
