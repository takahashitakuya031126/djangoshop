from django.test import TestCase

class ViewTest(TestCase):

    def test_first_page(self):
        response = self.client.get('/')
        assert response.status_code == 200
    
    def test_productlist_used_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shop/product_list.html')