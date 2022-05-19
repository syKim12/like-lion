from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request, 'product.html')

def productfirst(request):
    return render(request, 'productfirst.html')