from django.db import models
from products.models import Product
from profiles.models import UserProfile


class Wishlist(models.Model):
    """
    A Wishlist for each user that can hold multiple products.
    """
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE,
                                related_name='wishlist')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}'s Wishlist"


class WishlistItem(models.Model):
    """
    A specific product in a user's wishlist.
    """
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE,
                                 related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('wishlist', 'product')  # Prevents duplicates

    def __str__(self):
        return f"{self.product.name} in {self.wishlist.user}'s Wishlist"
