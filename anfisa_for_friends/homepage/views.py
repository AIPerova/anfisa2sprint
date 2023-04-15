from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Запишите в переменную ice_cream_list новый QuerySet
    ice_cream_list = IceCream.objects.values(
                    'id', 'title', 'price', 'description'
                    ).filter(
                    is_published=True,
                    is_on_main=True,
                    category__is_published=True
                    ).order_by(
                    'output_order',
                    'title')[:3]
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
