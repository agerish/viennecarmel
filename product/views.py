from django.shortcuts import render
from django.http import HttpResponse
from product.models import Product





def add(request,*args,**kwargs):
    nom='gerish je taime'
    product = Product.objects.get(id=4)
    context = {
        'name': product.name,
        'price': product.price,
        'description': product.description
    }
    return render(request,'abonner.html',context)

def contact(request,*args,**kwargs):
    return render(request,'contact.html')


def index(request,*args,**kwargs):
    return render(request,'index.html')
