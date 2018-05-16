from django.shortcuts import *
from .forms import SubscriberForm
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from products.models import *


def Subscriber(request):

    
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()


    return render(request, "Subscribers/Subscribers.html", locals())

def home(request):

    products_images = ProductImage.objects.filter(is_active=True, is_main=True, Product__is_active=True)
    products_images_phones = products_images.filter(Product__category__id=1)
    products_images_nouts = products_images.filter(Product__category__id=2)

    form = SubscriberForm(request.POST or None)

    if request.POST and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()

    return render(request, 'Subscribers/home.html', locals())



def about_us (request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'about_us/about_us.html', locals())

def doci (request):

    return render(request, 'doci/doci.html', locals())

def oprosnoi_list (request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'oprosnoi_list/oprosnoi_list.html', locals())

def ekspertiza (request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'ekspertiza/ekspertiza.html', locals())

def BMK (request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'BMK/BMK.html', locals())

def proektirovanie (request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'proektirovanie/proektirovanie.html', locals())

def kipia (request):
    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()
    return render(request, 'kipia/kipia.html', locals())
def kotli (request):

    return render(request, 'kotli/kotli.html', locals())

def kvartiri (request):

    products_images = ProductImage.objects.filter(is_active=True, is_main=True, Product__is_active=True)
    products_images_1 = products_images.filter(Product__category__id=1)
    products_images_2 = products_images.filter(Product__category__id=2)

    form = SubscriberForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()

    return render(request, 'products/kvartiri.html', locals())


