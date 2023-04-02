from django.contrib import admin
from houses.models import House

# Register your models here.


@admin.register(House)  # декоратор связывает класс HouseAdmin с моделью
class HouseAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]
