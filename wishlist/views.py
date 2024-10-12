from django.shortcuts import render, redirect, get_object_or_404
from .models import Wishlist, WishlistItem
from products.models import Product
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def view_wishlist(request):

    user_profile = get_object_or_404(UserProfile, user=request.user)
    wishlist, created = Wishlist.objects.get_or_create(user=user_profile)
    items = wishlist.items.all()

    return render(request, 'wishlist/wishlist.html', {'items': items,
                                                      'wishlist': wishlist})


@login_required
def add_to_wishlist(request, product_id):

    product = get_object_or_404(Product, id=product_id)
    user_profile = get_object_or_404(UserProfile, user=request.user)
    wishlist, created = Wishlist.objects.get_or_create(user=user_profile)

    # Check if the product is already in the wishlist
    if not WishlistItem.objects.filter(wishlist=wishlist,
                                       product=product).exists():
        WishlistItem.objects.create(wishlist=wishlist, product=product)
        messages.info(request,
                      f"{product.name} has been added to your wishlist!")
    else:
        messages.info(request,
                      f"{product.name} is already in your wishlist.")

    return redirect('product_detail', product_id=product.id)


@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(WishlistItem, id=item_id)
    item.delete()
    messages.info(request,
                  f'"{item.product.name}" has been removed from your wishlist.'
                  )
    return redirect('view_wishlist')
