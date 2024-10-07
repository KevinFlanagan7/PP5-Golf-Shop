from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist, WishlistItem
from products.models import Product
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def view_wishlist(request):
    # Get the UserProfile instance for the logged-in user
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # Try to fetch the Wishlist for the UserProfile instance
    wishlist, created = Wishlist.objects.get_or_create(user=user_profile)

    # Retrieve all items associated with the wishlist
    items = wishlist.items.all()  # Use the correct related_name 'items'

    # Pass the wishlist object and items to the template
    return render(request, 'wishlist/wishlist.html', {'items': items, 'wishlist': wishlist})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)

    if not WishlistItem.objects.filter(wishlist=wishlist, product=product).exists():
        WishlistItem.objects.create(wishlist=wishlist, product=product)
        messages.success(request, f"{product.name} has been added to your wishlist!")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")

    return redirect('wishlist:view_wishlist')


@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id)
    item.delete()
    return redirect('wishlist:view_wishlist')
