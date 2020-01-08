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
    
    # def test_user_except(self):
    #     with self.assertRaises(TypeError):
    #         User(1, 3, 4)

    def test_modify_bio(self):
        user = User("joe", "23/09/2000", "Bonn")
        self.assertTrue(user.modifyBio("test Bio"))

    def test_addFriend(self):
        user1 = User("joe", "23/09/2000", "Bonn")
        user2 = User("adam", "23/09/2000", "Bonn")
        self.assertTrue(user1.addFriend(user2))

    def test_joinGroup(self):
        user1 = User("joe", "23/09/2000", "Bonn")
        user2 = User("adam", "23/09/2000", "Bonn")
        group = Group("Food Lovers", user2)
        self.assertTrue(user1.joinGroup(group))

    def test_createPost(self):
        user = User("joe", "23/09/2000", "Bonn")
        self.assertTrue(user.createPost("test post"))

if __name__ == "__main__":
    unittest.main()

