from django.shortcuts import render


# Create your views here.

def index(request):
    context = {

    }
    return render(request, 'mainapp/index.html', context)


def cotalogs(request):
    light_items = [
        {
            'href1': "#",
            'image': "{% static 'img/csm_esprite-fs-01_1a739cd840.png' %}",  # а что сдесь надо что бы заработало?
            'title': "esprite",
            'href2': "#",
            'name': "ESPRITE™ FS",
        },
    ]
    context = {
        'title_page': 'каталог хатки',
        'light_items': light_items,
    }
    return render(request, 'mainapp/cotalogs.html', context)


def contacts(request):
    places = [
        {
            'phone': 'Контактный номер телефона интернет-магазина: 17-85-00',
            'address': 'Aдрес: туда-туда, потом на лево, через поле, направо от третьей пальмы хатка 15',
            'email': 'Begemotina@nightmail.ru',
        },
        {
            'phone': 'Контактный номер телефона интернет-палатки: 1111-00-222',
            'address': 'Aдрес: Красная площадь, дом 1',
            'email': 'Begemota_begemot@nightmail.ru',
        },
    ]
    context = {
        'title_page': 'контаткты хатки',
        'places': places,
    }
    return render(request, 'mainapp/contacts.html', context)
