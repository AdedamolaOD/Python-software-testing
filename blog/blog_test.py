import unittest
from blog import Blog

class BlogTest(unittest.TestCase):

    def setUp(self):
        self.blog = Blog("TestBlog", "Testauthor")

    def test_blog__init__(self):
        self.assertEqual(self.blog.title, "TestBlog")
        self.assertEqual(self.blog.author, "Testauthor")
        self.assertListEqual(self.blog.posts, [])

    def test_blog__repr__(self):

        self.

if __name__ == "__main__":
    unittest.main()