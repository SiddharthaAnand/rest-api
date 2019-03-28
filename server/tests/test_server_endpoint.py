import unittest
import json
from ..app import create_app


class TestEndpoint(unittest.TestCase):
    """
    Test case to test all the endpoints exposed to the user.
    """

    def setUp(self):
        """
        If you want the request context to be tested as well,
        use the app.test_client() with 'with' keyword.
        :return:
        """
        self.app = create_app("testing")
        self.app.testing = True
        self.client = self.app.test_client(self)

    def test_get_author(self):
        """
        Test GETting the author json object.
        :return:
        """
        response = self.client.get('/api/v1/author/Siddhartha Anand')
        self.assertEqual(response.status_code, 200)
        json_resp = json.loads(response.data)
        self.assertEqual(json_resp['status'], "ok")
        self.assertEqual(json_resp['total_results'], 1)
        self.assertEqual(json_resp['name'], "Siddhartha Anand")

    def test_say_hello(self):
        """ Test the app is alive or not."""
        # with self.client:
        response = self.client.get('/')
        json_resp = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json_resp, {'route': '/',
                                     'answer': 'hello there! I am alive :)'})

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
