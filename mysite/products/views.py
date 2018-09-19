from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.template import loader
from .models import Products

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'products/index.html'
    context_object_name = 'latest_product_list'
    def get_queryset(self):
        return Products.objects.order_by('created')[:5]

class DetailView(generic.DetailView):
    model = Products
    template_name = 'products/detail.html'

# def index(request):
#     latest_product_list = Products.objects.order_by('-created')[:5]
#     template = loader.get_template('products/index.html')
#     context = {
#         'latest_product_list': latest_product_list
#     }
#     return HttpResponse(template.render(context, request))
    # return HttpResponse("Hello, world. You're at the product index.")

# def detail(request,product_id):
#     product = get_object_or_404(Products,pk=product_id)
#     return render(request, 'products/detail.html', {'product': product})

def cart(request, product_id):
    product = get_object_or_404(Products,pk=product_id)
    try:
        selected_product = product.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Products.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': product,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_product.votes += 1
        selected_product.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(product.id,)))
