from django.shortcuts import render
from houses.models import House

# Create your views here.


def houses_list(request):  # функция представления, request - HTTP запрос посетителя)
    houses = House.objects.all()  # запрос к БД через ОРМ всех объектов в House (queryset)
    for house in houses:
        print(house.name, house.price, house.descriprion)
    # "houses" - путь, "houses_list.html" - название шаблона, {"houses" : houses} все объекты в модели
    return render(request, "houses/houses_list.html", {"houses": houses})
