import unittest
from app import db
from app.models import Comment,User


class CommentMOdelTest(unittest.TestCase):
   def setUp(self):
       self.user_hannah = User(username = 'hannah',password = 'hannah')
       self.new_comment = Comment(content='hannah')


   def test_check_instance_variable(self):
       self.assertEquals(self.new_comment.content,'hannah')