from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.


def petshop(request, c_slug=None):
    p = None
    if c_slug is not None:
        p = c_slug
        c_page = get_object_or_404(categ, slug=c_slug)
        pr = product.objects.filter(category=c_page)
    else:
        pr = product.objects.all()
    ct = categ.objects.all()
    paginator = Paginator(pr, 4)
    page = request.GET.get('page', 1)
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'ct': ct, 'pg': pro, 'p': p})


def detail(request, c_slug, prdt_slug):
    try:
        pr = product.objects.get(category__slug=c_slug, slug=prdt_slug)
    except Exception as e:
        raise e
    return render(request, "Details.html", {'pr': pr})


def search(request):
    pr = None
    ct = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
        paginator = Paginator(prod, 4)
        page = request.GET.get('page')
        try:
            pr = paginator.page(page)
        except (EmptyPage, InvalidPage):
            pr = paginator.page(1)
        ct = categ.objects.all()
    return render(request, 'home.html', {'pg': pr, 'ct': ct})
