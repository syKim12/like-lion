from django.urls import path
from product import views

urlpatterns = [
    path('', views.product),
    path('first/', views.productfirst)
]
