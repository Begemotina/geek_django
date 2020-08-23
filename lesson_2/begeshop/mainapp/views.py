from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')


def cotalogs(request):
    return render(request, 'mainapp/cotalogs.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')
