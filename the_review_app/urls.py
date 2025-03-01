from django.urls import path
from the_review_app import views

url_patterns = [ 
    path("", views.index, name="index"),
]