from django.db import models

# Create your models here.


class House(models.Model):
    name = models.CharField("название", max_length=50)
    price = models.IntegerField("цена")
    descriprion = models.TextField("Описание")
    photo = models.ImageField(
        "Фотография", upload_to="houses/photos", default="", blank=True)  # ImageField тип данных изображение,"Фотография" имя поля, houses/photos" - расположение

    # класс "Мета" внутри модели отвечает за ее базовые настройки (описательная информация)

    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"
        ordering = ["price"]

    def __str__(self) -> str:
        return self.name.upper()
