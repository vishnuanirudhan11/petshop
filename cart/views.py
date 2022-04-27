from django.shortcuts import render,redirect,get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def cart(request,tot=0,count=0,ct_items=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.price*i.quan)
            count+= i.quan
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',{'cl':ct_items,'t':tot,'cn':count})

def c_id(request):
    id=request.session.session_key
    if not id:
        id=request.session.create()
    return id

def add_cart(request,product_id):
    prod=product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct =cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=items.objects.get(prodt=prod,cart=ct)
        if c_items.quan < c_items.prodt.stock:
            c_items.quan+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(prodt=prod,quan=1,cart=ct)
        c_items.save()

    return redirect('cart')


def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(product,id=product_id)
    c_items=items.objects.get(prodt=prod,cart_id=ct)
    if c_items.quan>1:
        c_items.quan-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart')


def delete(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(product,id=product_id)
    c_items=items.objects.get(prodt=prod,cart_id=ct)
    c_items.delete()
    return redirect('cart')

def deleteall(request):
    cartitems=items.objects.all()
    cartitems.delete()
    return redirect('cart')
