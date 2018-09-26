from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
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
        selected_product =product
    except (KeyError, Product.DoesNotExist):
        # Redisplay the product form.
        return render(request, 'product/detail.html', {
            'product': product,
            'error_message': "You didn't select a choice.",
        })
    else:
        print('here>>>>')
        """ Add item to cart"""
        Cart.objects.create(product=selected_product,user=1)
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('product'))
