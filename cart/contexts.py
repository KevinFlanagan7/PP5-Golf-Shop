from django.shortcuts import get_object_or_404
from products.models import Product

def cart_contents(request):

    cart_items = []
    grand_total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            grand_total += item_data * product.price
            product_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                grand_total += quantity * product.price
                product_count += quantity
                cart_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                    'size': size,
                })
    
    context = {
        'cart_items': cart_items,
        'grand_total': grand_total,
        'product_count': product_count, 
    }

    return context