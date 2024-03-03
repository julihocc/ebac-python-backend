# from django.shortcuts import render
# from .models import Cart

# def checkout_view(request):
#     # Assuming you have a cart instance (you might want to get or create one based on session or user)
#     cart = Cart.objects.first()  # Example: getting the first cart
#     context = {'message': cart.checkout()}
#     return render(request, 'store/checkout.html', context)

from django.shortcuts import render
from .models import Cart

def checkout_view(request):
    # This line attempts to get the first cart object, or creates a new one if none exist
    cart, created = Cart.objects.get_or_create(id=1) # Example: using a fixed ID for simplicity
    context = {'message': cart.checkout()}
    return render(request, 'store/checkout.html', context)
