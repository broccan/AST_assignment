import unittest
import sys
sys.path.append(".")
sys.path.append('..')
from facebook.User import User
from facebook.Group import Group
from facebook.Timeline import Timeline
from facebook.Post import Post


class user_unit_tests(unittest.TestCase):
    def test_user_init(self):
        try:
            User("joe", "23/09/2000", "Bonn")
        except:
            self.fail("Unexpected exception when initialising user")
    
    def test_user_except(self):
        with self.assertRaises(TypeError):
            User(1, 3, 4)