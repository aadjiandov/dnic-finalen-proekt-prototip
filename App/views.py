from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import VacuumCleaner, CartItem


def robots_list(request):
    robots = VacuumCleaner.objects.all()
    return render(request, 'robots.html', {'robots': robots})


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def robot_search(request):
    search_query = request.GET.get('search')
    robots = VacuumCleaner.objects.filter(name__icontains=search_query)
    return render(request, 'robots.html',
                  {'robots': robots, 'search_query': search_query})


def cart(request):
    cart = request.session.get('cart', {})  # Retrieve the cart from the session

    cart_items = []
    cart_total = 0

    for product_id, quantity in cart.items():
        robot = VacuumCleaner.objects.get(id=product_id)
        subtotal = robot.price * quantity
        cart_items.append({
            'product': robot,
            'quantity': quantity,
            'subtotal': subtotal
        })
        cart_total += subtotal

    context = {
        'cart_items': cart_items,
        'cart_total': cart_total,
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, robot_id):
    product = VacuumCleaner.objects.get(id=robot_id)
    cart = Cart(request)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product=product, quantity=quantity)
    return redirect('cart')


def checkout(request):
    if request.method == 'POST':
        # Retrieve the cart items from the session
        cart = request.session.get('cart', {})

        # Process the checkout logic
        # ... (e.g., create an order, update inventory, etc.)

        # Clear the cart after successful checkout
        request.session['cart'] = {}

        # Redirect to a success page or order confirmation page
        return redirect('order_confirmation')

        # Render the checkout form
    return render(request, 'checkout.html')


def update_cart(cart, robot_id):
    updated_cart = {}
    for item_id, item in cart.items():
        if item_id != robot_id:
            updated_cart[item_id] = item
    return updated_cart


def delete_from_cart(request, robot_id):
    cart = request.session.get('cart', {})
    updated_cart = update_cart(cart, robot_id)
    request.session['cart'] = updated_cart
    return redirect('cart')


def update_quantity(request, product_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart = Cart(request)
        cart.update_quantity(product_id, quantity)
        return JsonResponse({'message': 'Quantity updated successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)
