from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Product, Cart, Wishlist
from django.contrib import messages
import os
import json
import requests
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from decimal import Decimal
from django.shortcuts import render, redirect
from app.models import Product, Order, Cart
from django.contrib.auth.decorators import login_required, user_passes_test


from .models import Product, Cart, Order, Transaction
# 🏠 Home Page
def home(request):
    products = Product.objects.all()
    return render(request, 'app/index.html', {'products': products})


# 🧀 Category Page
class CategoryView(View):
    def get(self, request, val):
        products = Product.objects.filter(category=val)
        return render(request, 'app/category.html', {'products': products, 'val': val})


# 📦 Product Detail Page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'app/productdetails.html', {'product': product})


# 📞 Contact Page
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        try:
            send_mail(
                f"New Contact Message: {subject}",
                f"From: {name} <{email}>\n\n{message}",
                'sharatacharjee6@gmail.com',
                ['sharatacharjee6@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except:
            messages.error(request, "Sorry! Something went wrong. Please try again later.")
        return redirect('contact')

    return render(request, 'app/contact.html')


# ℹ️ About Page
def about(request):
    return render(request, 'app/about.html')


# ===============================
# 🛒 CART FUNCTIONS
# ===============================
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.title} added to your cart.")
    return redirect('home')


@login_required
def remove_from_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item removed from cart.")
    return redirect('cart')


@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.discounted_price * item.quantity for item in cart_items)
    return render(request, 'app/cart.html', {'cart_items': cart_items, 'total': total})


# ===============================
# 💖 WISHLIST FUNCTIONS
# ===============================
@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)

    if not created:
        messages.info(request, f"{product.title} is already in your wishlist.")
    else:
        messages.success(request, f"{product.title} added to your wishlist.")
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, item_id):
    wishlist_item = get_object_or_404(Wishlist, id=item_id, user=request.user)
    wishlist_item.delete()
    messages.success(request, "Item removed from wishlist.")
    return redirect('wishlist')


@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'app/wishlist.html', {'wishlist_items': wishlist_items})


# ===============================
# 🛍️ BUY NOW
# ===============================
@login_required
def buy_now(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f"{product.title} added to your cart. Proceed to checkout!")
    return redirect('cart')


# ===============================
# 🔍 SEARCH FUNCTION
# ===============================
def search(request):
    query = request.GET.get('query', '').strip()
    if query:
        products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return render(request, 'app/search_results.html', {'products': products, 'query': query})
    else:
        messages.warning(request, "Please enter something to search")
        return render(request, 'app/search_results.html', {'products': [], 'query': query})


# ===============================
# 🔑 USER REGISTRATION
# ===============================
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists! Try another.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Registration successful! You can now login.")
        return redirect('login')

    return render(request, 'app/register.html')

@login_required
def update_cart(request, item_id):
    cart_item = get_object_or_404(Cart, id=item_id, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('cart')
@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.discounted_price * item.quantity for item in cart_items)
    return render(request, 'app/cart.html', {'cart_items': cart_items, 'total': total})
# views.py
@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.discounted_price * item.quantity for item in cart_items)
    return render(request, 'app/checkout.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, "✅ Your product added to cart successfully! Check your cart section.")
    return redirect('cart')
# Example: user clicks "Buy Now" -> create minimal order then start checkout
def buy_now(request, product_id):
    if not request.user.is_authenticated:
        messages.info(request, "Please login to buy.")
        return redirect('login')

    product = get_object_or_404(Product, id=product_id)
    # Create an Order for this single product (you can customize quantity)
    order = Order.objects.create(user=request.user, total=Decimal(product.discounted_price))
    # create initial transaction record
    txn = Transaction.objects.create(order=order, gateway='bkash', amount=order.total, status='initiated')
    # Redirect to a checkout starter view and pass order id
    return redirect('checkout_start', order_id=order.id, gateway='bkash')

# Very simple start-checkout view (gateway param: 'bkash' or 'nagad')
def checkout_start(request, order_id, gateway='bkash'):
    order = get_object_or_404(Order, id=order_id)

    if gateway == 'bkash':
        # === bKash flow (conceptual) ===
        # 1) obtain auth token
        token_endpoint = f"{settings.BKASH_BASE_URL}/token/grant"   # placeholder
        auth_payload = {
            "app_key": settings.BKASH_APP_KEY,
            "app_secret": settings.BKASH_APP_SECRET
        }
        try:
            r = requests.post(token_endpoint, json=auth_payload, timeout=15)
            r.raise_for_status()
            token_data = r.json()
            id_token = token_data.get('id_token') or token_data.get('idToken')
        except Exception as e:
            messages.error(request, "Payment service unavailable. Try again.")
            return redirect('home')

        # 2) create payment (provider uses token & specific payload)
        create_payment_endpoint = f"{settings.BKASH_BASE_URL}/checkout/create"
        headers = {
            'Authorization': id_token,
            'Content-Type': 'application/json'
        }
        create_payload = {
            "amount": str(order.total),
            "currency": "BDT",
            "intent": "sale",
            "merchantInvoiceNumber": f"ORD-{order.id}"
            # plus any other fields provider requires
        }

        try:
            r2 = requests.post(create_payment_endpoint, json=create_payload, headers=headers, timeout=15)
            r2.raise_for_status()
            create_resp = r2.json()
            # provider will respond with a payment session id or a redirect URL
            # example placeholders:
            payment_url = create_resp.get('paymentURL') or create_resp.get('bkashURL')
            provider_payment_id = create_resp.get('paymentID') or create_resp.get('paymentID')
        except Exception as e:
            messages.error(request, "Unable to start payment. Try again.")
            return redirect('home')

        # save provider tx id to our Transaction
        txn = order.transactions.first()
        txn.provider_transaction_id = provider_payment_id
        txn.raw_response = create_resp
        txn.save()

        # redirect user to the payment_url (or render a page + JS to open gateway popup)
        if payment_url:
            return redirect(payment_url)
        else:
            # if provider expects client JS to open wallet, render a page that will trigger the wallet
            return render(request, 'app/pay_redirect.html', {'create_resp': create_resp})

    elif gateway == 'nagad':
        # === Nagad flow (conceptual) ===
        # Similar: request token/initiate payment -> get redirect URL -> redirect user
        initiate_url = f"{settings.NAGAD_BASE_URL}/api/merchant/v2/initiate/"
        payload = {
            "merchantId": settings.NAGAD_MERCHANT_ID,
            "orderId": f"ORD-{order.id}",
            "amount": str(order.total),
            # ... other fields required
        }
        try:
            r = requests.post(initiate_url, json=payload, timeout=15)
            r.raise_for_status()
            resp = r.json()
            pay_url = resp.get('paymentURL') or resp.get('payment_url')
            txn = order.transactions.first()
            txn.provider_transaction_id = resp.get('transaction_id')
            txn.raw_response = resp
            txn.save()
            return redirect(pay_url)
        except Exception as e:
            messages.error(request, "Unable to start Nagad payment.")
            return redirect('home')

    else:
        messages.error(request, "Unsupported payment method.")
        return redirect('home')

def buy_now(request, product_id):
    product = Product.objects.get(id=product_id)


    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        payment_method = request.POST.get("payment_method")
        last4digit = request.POST.get("last4digit")

        # You can save in DB (optional)
        # Order.objects.create(...)

        messages.success(request, "Your product delivery will process soon!")
        return redirect('home')

    return render(request, 'app/buy_now.html', {"product": product})
    

# === Webhook / callback endpoints: provider calls this after payment ===

# bKash callback (provider -> our endpoint); must be public and HTTPS
@csrf_exempt
def bkash_callback(request):
    # Providers will send POST JSON with status and transaction id
    payload = json.loads(request.body.decode('utf-8'))
    # Example fields: {"paymentID": "...", "trxID": "...", "status":"success"}
    provider_txn = payload.get('trxID') or payload.get('paymentID')
    invoice = payload.get('merchantInvoiceNumber') or payload.get('merchantInvoiceNo')
    # find our order using invoice or provider_txn mapping
    # (How you identify ~= depends on provider's callback fields)
    try:
        order_id = int(invoice.split('-')[-1])
        order = Order.objects.get(id=order_id)
    except Exception:
        return JsonResponse({"error":"order_not_found"}, status=400)

    txn = order.transactions.first()
    # verify signature/hmac if provider sends one (VERY IMPORTANT)
    # TODO: verify signature here

    # update status
    if payload.get('status') in ('success','completed','paid'):
        order.status = 'paid'
        order.save()
        txn.status = 'success'
        txn.provider_transaction_id = provider_txn
        txn.raw_response = payload
        txn.save()
    else:
        order.status = 'failed'
        order.save()
        txn.status = 'failed'
        txn.raw_response = payload
        txn.save()

    return JsonResponse({"ok": True})


# Nagad callback
@csrf_exempt
def nagad_callback(request):
    payload = json.loads(request.body.decode('utf-8'))
    # verify signature; update order/txn similarly
    # (fields differ per provider)
    return JsonResponse({"ok": True})
# Only staff can access
def staff_check(user):
    return user.is_staff

@login_required
@user_passes_test(staff_check)
def admin_dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    cart_items = Cart.objects.all()
    context = {
        'products': products,
        'orders': orders,
        'cart_items': cart_items,
    }
    return render(request, 'dashboard/admin_dashboard.html', context)