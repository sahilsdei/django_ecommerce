from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader
from django.views import generic
from .models import Cart

# Create your views here.
class IndexView(generic.ListView):
    latest_product_list = Cart.objects.order_by('-created')[:5]
    template = loader.get_template('product/index.html')
    context = 'latest_cart_list'
    def get_queryset(self):
        return Cart.objects.order_by('created')[:5]

class DetailView(generic.DetailView):
    return''