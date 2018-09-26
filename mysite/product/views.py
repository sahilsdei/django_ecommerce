from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Product
from cart.models import Cart
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'product/index.html'
    context_object_name = 'latest_product_list'
    def get_queryset(self):
        return Product.objects.order_by('created')[:5]

class DetailView(generic.DetailView):
    model = Product
    template_name = 'product/detail.html'

def cart(request, product_id):
    product = get_object_or_404(Product,pk=product_id)
    try:
        cart = Cart.objects.get(product=product_id)
    except Cart.DoesNotExist:
        cart = None

    if(cart):
        cart.qty +=1 
        cart.save()
    else:
        Cart.objects.create(product=product,user=1,qty=1)
    return redirect('/product')