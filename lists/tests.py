from django.urls import resolve
from django.test import TestCase
from lists.views import home_page


class HomePageTest(TestCase):
    """home page test"""

    def test_root_url_resolves_to_home_page_view(self):
        """test: root url is converted to a home page view"""
        found = resolve('/')
        self.assertEqual(found.func, home_page)
