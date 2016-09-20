import blog
import unittest


class RoutingLoginTestCase(unittest.TestCase):

    def setUp(self):
        self.app = blog.app.test_client()

    def login(self, username, password):
        return self.app.post('/login', data=dict(username=username, password=password),
                             follow_redirects=True)

    def test_login_page_get(self):
        response_get = self.app.get('/login')
        self.assertEqual(response_get.status_code, 200)
        self.assertIn('Login', response_get.data)
        self.assertIn('Password', response_get.data)

    def test_login_page_post(self):
        # if credentials are right
        response_post = self.login('admin', 'admin')
        self.assertEqual(response_post.status_code, 200)
        self.assertIn('You were logged in', response_post.data)
        # if credentials are wrong
        response_post = self.login('123', 'admin')
        self.assertIn('Invalid username/password', response_post.data)
        response_post = self.login('admin', '123')
        self.assertIn('Invalid username/password', response_post.data)

    def test_login_page_other(self):
        response_put = self.app.put('/login')
        response_delete = self.app.delete('/login')
        self.assertEqual(response_put.status_code, 405)
        self.assertEqual(response_delete.status_code, 405)

if __name__ == '__main__':
    unittest.main()
