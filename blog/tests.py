from django.test import TestCase, Client

class BlogTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_index_access(self):
        res = self.c.get('/')
        # 200 → OK
        # 302 → Redirect
        # 404 → Not found
        print(res.status_code)
        self.assertEqual(200, res.status_code)

    def test_fial_access(self):
        res = self.c.get('/unknown')
        print(res.status_code)
        self.assertEqual(404, res.status_code)
