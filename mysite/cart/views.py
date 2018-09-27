from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from .models import Cart

# Create your views here.
class IndexView(generic.ListView):
    # latest_cart_list = Cart.objects.order_by('-created')
    template_name = 'cart/index.html'
    context_object_name = 'latest_cart_list'
    def get_queryset(self):
        return Cart.objects.order_by('product_id')[:5]

# class DetailView(generic.DetailView):
#     model = Cart
#     template_name = 'cart/index.html'


def checkout(latest_cart_list):
    print('>>>>>>>>',latest_cart_list)
    return redirect('/product')