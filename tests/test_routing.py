import unittest
from blog_flask.blog import app


class RoutingTestCase(unittest.TestCase):

    def test_startpage(self):
        response_get = self.app.get('/')
        response_post = self.app.post('/')
        response_delete = self.app.delete('/')
        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(response_post.status_code, 405)
        self.assertEqual(response_delete.status_code, 405)

if __name__ == '__main__':
    unittest.main()
