def cart_count(request):
    from .cart import Cart
    cart = Cart(request)
    return {'cart_count': len(cart)}