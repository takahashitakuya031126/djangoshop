from django.test import TestCase
from shop.models import Category

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