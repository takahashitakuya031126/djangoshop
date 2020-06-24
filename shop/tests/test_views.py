from django.test import TestCase
from django.urls import reverse
from shop.models import Category, Product

PRODUCT_LIST_URL = reverse('shop:all_product')

def sample_category(name, slug, description):
    return Category.objects.create(
        name = name,
        slug = slug,
        description = description
    )

def sample_product(name, slug, description, category, price, stock, available):
    return Product.objects.create(
        name = name,
        slug = slug,
        description = description,
        category = category,
        price = price,
        stock = stock,
        available = available
    )

class ViewTest(TestCase):

    def test_first_page(self):
        response = self.client.get('/')
        assert response.status_code == 200
    
    def test_productlist_used_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shop/product_list.html')
    
    def test_retrieve_products(self):
        c = sample_category(
            name = 'Black Urban Cushion',
            slug = 'black-urban-cushion',
            description = 'This is a category for black urban cushion'
        )
 
        sample_product(
            name = 'dog',
            slug = 'dog',
            description = 'Dogs are intelligent animals!',
            category = c,
            price = 30.2,
            stock = 30,
            available = True
        )
 
        sample_product(
            name = 'rabbit',
            slug = 'rabbit',
            description = 'rabits are so cute animals!',
            category = c,
            price = 60.1,
            stock = 2,
            available = True
        )
 
        self.product3 = Product.objects.create(
            name = 'cat',
            slug = 'cat',
            description = 'cats are loved by everyone!',
            category = c,
            price = 60.1,
            stock = 2,
            available = False
        )
 
        response = self.client.get(PRODUCT_LIST_URL)
 
        assert 'dog' in [product.name for product in response.context['products']]
        assert 'rabbit' in [product.name for product in response.context['products']]
        assert 'cat' not in [product.name for product in response.context['products']]