import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_home(self):
        from .views import home
        request = testing.DummyRequest()
        info = home(request)
        self.assertEqual(info['project'], 'scraper')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from scraper import main
        app = main({})
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/', status=200)
        self.assertTrue(b'<!DOCTYPE html>' in res.body)
