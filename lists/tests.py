from django.test import TestCase


class HomePageTest(TestCase):
    """home page test"""

    def test_uses_home_template(self):
        """test: using a home template"""
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
