from django.urls import path
from . import views
app_name = 'cart'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('checkout',views.checkout,name="checkout")
]
