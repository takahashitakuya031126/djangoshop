from django.test import TestCase
from django.utils import timezone
from cart.models import Cart

class ModelTest(TestCase):

    def test_create_cart(self):
        
        Cart.objects.create(
            cart_id='USERONLY',
            date_added=timezone.now
        )

        c = Cart.objects.all()[0]
        assert str(c) == c.cart_id