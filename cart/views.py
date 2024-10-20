from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
    )
from django.contrib import messages
from products.models import Product


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add a quantity of the product to the cart """

    product = get_object_or_404(Product, pk=item_id)

    min_quantity = 1
    max_quantity = 99

    # Gets the quantity from the POST request and validate it
    try:
        quantity = int(request.POST.get('quantity', 0))
    except (ValueError, TypeError):
        quantity = 0

    redirect_url = request.POST.get('redirect_url', '/')
    size = request.POST.get('product_size', None)
    cart = request.session.get('cart', {})

    # Check if quantity is within the valid range
    if quantity < min_quantity or quantity > max_quantity:
        messages.error(
            request,
            (
                f'Please enter a quantity between {min_quantity}'
                f'and {max_quantity}.'
            )
        )
        return redirect(redirect_url)

    if size:
        if item_id in list(cart.keys()):
            if size in cart[item_id]['items_by_size'].keys():
                cart[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size} {product.name} quantity to '
                    f'{cart[item_id]["items_by_size"][size]}'
                )
            else:
                cart[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size} {product.name} to your cart'
                )
        else:
            cart[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size} {product.name} to your cart'
            )
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {cart[item_id]}'
            )
        else:
            cart[item_id] = quantity
            messages.success(request, f'{product.name} added to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)

    min_quantity = 1
    max_quantity = 99

    # Gets the quantity from the POST request and validate it
    try:
        quantity = int(request.POST.get('quantity', 0))
    except (ValueError, TypeError):
        quantity = 0

    size = request.POST.get('product_size', None)
    cart = request.session.get('cart', {})

    # Check if quantity is within the valid range
    if quantity < min_quantity or quantity > max_quantity:
        messages.error(
            request,
            f'Please enter a quantity between {min_quantity} '
            f'and {max_quantity}.'
        )
        return redirect(reverse('view_cart'))

    if size:
        if quantity > 0:
            cart[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size} {product.name} quantity '
                f'to {cart[item_id]["items_by_size"][size]}'
            )
        else:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request,
                f'Removed size {size} {product.name} from your cart'
            )
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(
                request, f'Updated {product.name} quantity to {cart[item_id]}'
            )
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        cart = request.session.get('cart', {})

        if size:
            del cart[item_id]['items_by_size'][size]
            if not cart[item_id]['items_by_size']:
                cart.pop(item_id)
            messages.success(
                request, f'Removed size {size} {product.name} from your cart'
            )
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {product.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
