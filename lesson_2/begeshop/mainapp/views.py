from django.shortcuts import render


# Create your views here.

def index(request):
    context = {

    }
    return render(request, 'mainapp/index.html', context)


def cotalogs(request):
    context = {
        'title_page': 'каталог хатки',
    }
    return render(request, 'mainapp/cotalogs.html', context)


def contacts(request):
    context = {
        'title_page': 'контаткты хатки',
    }
    return render(request, 'mainapp/contacts.html', context)
