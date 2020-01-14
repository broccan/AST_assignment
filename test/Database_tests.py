#!/usr/bin/env python3
import unittest

import sys
sys.path.append(".")

from facebook.Database import Database
from facebook.User import User

class DatabaseUnitTest(unittest.TestCase):

    def test_create_instance_test(self):
        db = Database.getInstance()

        self.assertEqual(db.__class__, Database)

    def test_add_user_to_database(self):
        db = Database.getInstance()

        name = 'Alan'
        birthday = '22.12.1995'
        location = 'Sankt Augustin'
        user = User(name, birthday, location)

        self.assertTrue(db.add('users', user.name, user))
        self.assertEqual(user, db.get('users', user.name))

    def test_get_all_from_database(self):
        db = Database.getInstance()

        users = db.getAll('users')

        self.assertEqual(dict, users.__class__)

    def test_delete_element(self):
        db = Database.getInstance()

        name = 'Samuel'
        birthday = '02.08.1996'
        location = 'Sankt Augustin'
        user = User(name, birthday, location)
        
        db.add('users', user.name, user)

        self.assertTrue(db.delete('users', user.name))

if __name__ == '__main__':
    unittest.main()   