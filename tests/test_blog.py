import unittest
from app import db
from app.models import Blog,User


class BlogMOdelTest(unittest.TestCase):
   def setUp(self):
       self.user_kitsao = User(username = 'kitsao',password = 'kitsao')
       self.new_blog = Blog(content='kitsao')


   def test_check_instance_variable(self):
       self.assertEquals(self.new_blog.content,'kitsao')



