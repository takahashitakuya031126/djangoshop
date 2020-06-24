from django.test import TestCase
from shop.models import Category, Product

class ModelTest(TestCase):

    def test_create_category(self):
        name = 'Black Urban Cushion'
        slug = 'black-urban-cushion'
        description = 'This is a category for black urban cushion'

        Category.objects.create(
            name = name,
            slug = slug,
            description = description
        )

        c = Category.objects.all()[0]
        assert str(c) == c.name
    
    def test_create_product(self):
        c = Category.objects.create(
            name = 'Black Urban Cushion',
            slug = 'black-urban-cushion',
            description = 'This is a category for black urban cushion')
 
        Product.objects.create(
            name = 'pag dog',
            slug = 'pag-dog',
            description = 'Pag dog is as big as cats',
            category = c,
            price = 30.2,
            stock = 30,
            available = True
        )
        
        p = Product.objects.all()[0]
        assert str(p) == p.name