from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # ================= HOME =================
    path('', views.home, name='home'),

    # ================= AUTH =================
    # ❌ login removed (handled by allauth)

    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),

    # ================= CATEGORY =================
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),

    # ================= PRODUCT =================
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # ================= CART =================
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart, name='cart'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),

    # ================= WISHLIST =================
    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),

    # ================= PAGES =================
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),

    # ================= SEARCH =================
    path('search/', views.search, name='search'),

    # ================= BUY / CHECKOUT =================
    path('buy-now/<int:product_id>/', views.buy_now, name='buy_now'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/<int:order_id>/<str:gateway>/', views.checkout_start, name='checkout_start'),

    # ================= PAYMENT CALLBACK =================
    path('callbacks/bkash/', views.bkash_callback, name='bkash_callback'),
    path('callbacks/nagad/', views.nagad_callback, name='nagad_callback'),

    # ================= ADMIN DASHBOARD =================
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
