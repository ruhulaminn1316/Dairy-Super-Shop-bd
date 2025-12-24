from django.contrib import admin
from .models import Product  # make sure to use .models to import from current app

# Register your Product model
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'selling_price', 'discounted_price', 'category','image']
    list_filter = ['category']        # optional: filter by category
    search_fields = ['title', 'description']  # optional: search box
