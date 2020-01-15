import unittest
import sys
from facebook.Timeline import Timeline
sys.path.append(".")
sys.path.append('..')


class TimelineUnitTests(unittest.TestCase):
    def test_addPost(self):
        timeline = Timeline()
        timeline.addPost("test post")
        self.assertEqual(timeline.posts[0],"test post")
