from django.urls import path
from . import views


urlpatterns=[
    path('cart_details/',views.cart,name='cart'),
    path('add_cart/<int:product_id>',views.add_cart,name='add_cart'),
    path('min/<int:product_id>', views.min_cart, name='min'),
    path('delete/<int:product_id>', views.delete, name='delete'),
    path('deleteall/',views.deleteall,name='deleteall')
]