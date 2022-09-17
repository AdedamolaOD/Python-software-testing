from unittest import TestCase
from post import Post

class PostTest(TestCase):

    def test_post_init(self):
        post = Post("Tech Biggest Boy", "Nigerian-born 18 yr old software engineer becomes CEO of Cashapp")

        self.assertEqual(post.title, "Tech Biggest Boy")
        self.assertEqual(post.content, "Nigerian-born 18 yr old software engineer becomes CEO of Cashapp")

