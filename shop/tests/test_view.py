from django.test import TestCase

class ViewTest(TestCase):

    def test_first_page(self):
        response = self.client.get('/')
        assert response.status_code == 200