class Timeline:
    """
    Class for implementing Timeline

    """
    def __init__(self):
        self.posts = []

    def addPost(self, post):
        """
        Method to add posts to timeline

        Parameters
        ----------
        post: Post

        Returns
        -------
        None      
        """
        self.posts.append(post)
        
    def showPosts(self):
        """
        Displays all posts created by user in  ordered manner

        Parameters
        -----------
        None
        
        Returns
        -------
        None    

        """
        for post in self.posts:
            post.showPost()
    