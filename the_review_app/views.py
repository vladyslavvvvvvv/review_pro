from django.shortcuts import render
from the_review_app.models import Product, Review
from django.http import HttpResponse

def index(request):
    context = {
        "render_string: Hello, world"
    }
    return render(request, template_name="", context=context)

def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, template_name="the_review_app")