import unittest
import sys
from facebook.Post import Post
sys.path.append(".")
sys.path.append('..')


class PostUnitTests(unittest.TestCase):
    def test_addLike(self):
        post = Post("test_user","test post")
        post.addLike("liking_user")
        self.assertEqual(post.likes[0],"liking_user")
