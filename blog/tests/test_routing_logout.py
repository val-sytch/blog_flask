import unittest
import blog


class RoutingLogoutTestCase(unittest.TestCase):

    def setUp(self):
        self.app = blog.app.test_client()

    def test_logout_page_get(self):
        response_get = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response_get.status_code, 200)
        self.assertIn('You were logged out', response_get.data)

    def test_logout_page_other(self):
        response_post = self.app.post('/logout')
        response_put = self.app.put('/logout')
        response_delete = self.app.delete('/logout')
        self.assertEqual(response_post.status_code, 405)
        self.assertEqual(response_put.status_code, 405)
        self.assertEqual(response_delete.status_code, 405)

if __name__ == '__main__':
    unittest.main()
