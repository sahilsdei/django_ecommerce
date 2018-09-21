from django.urls import path
from . import views
app_name = 'product'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:product_id>/cart/',views.cart,name="cart")
]