from . models import Cart,CartItem
from . views import _cart_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return{} #The return keyword in Python exits a function and tells Python to run the rest of the main program.
    else:
        try:
            cart=Cart.objects.filter(cart_id=_cart_id(request))
            cart_items=CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count +=cart_item.quantity
        except Cart.DoesNotExist:
            item_count =0
    return dict(item_count=item_count)