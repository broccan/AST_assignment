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
        self.owner    = owner
        self.content  = content

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
        print("{} by {}".format(self.content, self.owner.full_name))

