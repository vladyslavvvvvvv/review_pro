from django.contrib import admin

from .models import Product, Review

# Register your models here.
admin.site.register(Review),
admin.site.register(Product)