from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/',views.products, name='products'),
    path('customers/<str:pk_test>/',views.customer,name='customer'),
    path('create_orders/',views.createOrder,name='create_order'),
    path('update_orders/<str:pk>/',views.updateOrder,name='update_order'),
    path('delete_orders/<str:pk>/',views.deleteOrder,name='delete_order')
]