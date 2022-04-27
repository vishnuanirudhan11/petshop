from django.urls import path
from.import views

app_name='myapp'
urlpatterns=[
    path('petshop/', views.petshop, name='petshop'),
    path('hello/<slug:c_slug>/', views.petshop, name='petshop1'),
    path('my/<slug:c_slug>/<slug:prdt_slug>/', views.detail, name='detail'),
    path('search1/', views.search, name='search1')

]
