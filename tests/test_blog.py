import unittest
from app import db
from app.models import Blog,User


class BlogMOdelTest(unittest.TestCase):
   def setUp(self):
       self.user_hannah = User(username = 'hannah',password = 'hannah')
       self.new_blog = Blog(content='hannah')


   def test_check_instance_variable(self):
       self.assertEquals(self.new_blog.content,'hannah')



