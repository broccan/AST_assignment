#!/usr/bin/env python3
import unittest

import sys
sys.path.append(".")

from facebook.User import User
from facebook.Group import Group
from facebook.Post import Post

class GroupUnitTests(unittest.TestCase):

    def test_create_group(self):
        group_name = 'MyGroup'

        name = 'Alan'
        birthday = '22.12.1995'
        location = 'Sankt Augustin'
        admin = User(name, birthday, location)

        group = Group(group_name, admin)

        self.assertEqual(group.name, group_name)
        self.assertEqual(group.admin, admin)
    
    def test_add_remove_post(self):
        group_name = 'MyGroup'

        name = 'Alan'
        birthday = '22.12.1995'
        location = 'Sankt Augustin'
        admin = User(name, birthday, location)

        group = Group(group_name, admin)

        content_post = 'C++ rules'
        post = Post(admin, content_post)

        group.addPost(post)
        
        self.assertEqual(post.content, group.posts[0].content)
        self.assertTrue(group.removePost(post))
        self.assertFalse(group.removePost(post))

    def test_add_remove_user(self):
        group_name = 'MyGroup'

        name = 'Alan'
        birthday = '22.12.1995'
        location = 'Sankt Augustin'
        admin = User(name, birthday, location)

        name_1 = 'Javier'
        birthday_1 = '00.00.0000'
        location_1 = 'Barcelona'
        user_1 = User(name_1, birthday_1, location_1)

        name_2 = 'Rodrigo'
        birthday_2 = '00.00.0000'
        location_2 = 'Aguascalientes'
        user_2 = User(name_2, birthday_2, location_2)

        group = Group(group_name, admin)

        group.addUser(user_1)
        group.addUser(user_2)
        
        self.assertEqual(len(group.users), 2)
        self.assertTrue(group.removeUser(admin, user_1))
        self.assertFalse(group.removeUser(admin, user_1))
        self.assertTrue(group.removeUser(admin, user_2))
        self.assertFalse(group.removeUser(admin, user_2))

if __name__ == '__main__':
    unittest.main()   