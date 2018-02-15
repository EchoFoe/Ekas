from django.shortcuts import *
from .forms import SubscribersForm
from django.shortcuts import render


def Subscribers(request):

    form = SubscribersForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(form.cleaned_data["name"])
        new_form = form.save()

    # return render(request, 'Subscribers/Subscribers.html', locals())
    return render(request, 'footer.html', locals())

def home(request):

    return render(request, 'Subscribers/home.html', locals())

def about_us (request):

    return render(request, 'about_us/about_us.html', locals())

def doci (request):

    return render(request, 'doci/doci.html', locals())

def oprosnoi_list (request):

    return render(request, 'oprosnoi_list/oprosnoi_list.html', locals())

def ekspertiza (request):

    return render(request, 'ekspertiza/ekspertiza.html', locals())

def BMK (request):

    return render(request, 'BMK/BMK.html', locals())

def proektirovanie (request):

    return render(request, 'proektirovanie/proektirovanie.html', locals())

def kipia (request):

    return render(request, 'kipia/kipia.html', locals())
def kotli (request):

    return render(request, 'kotli/kotli.html', locals())