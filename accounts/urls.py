from django.urls import path
from . import views

urlpatterns=[
    path('logout/',views.logout,name='logout'),
    path('',views.login,name='login'),
    path('reg',views.reg,name='reg')
]