import blog
import unittest


class RoutingStartpageTestCase(unittest.TestCase):

    def setUp(self):
        self.app = blog.app.test_client()

    def test_start_page(self):
        response_get = self.app.get('/')
        response_post = self.app.post('/')
        response_put = self.app.put('/')
        response_delete = self.app.delete('/')
        self.assertEqual(response_get.status_code, 200)
        self.assertEqual(response_post.status_code, 405)
        self.assertEqual(response_put.status_code, 405)
        self.assertEqual(response_delete.status_code, 405)

if __name__ == '__main__':
    unittest.main()
