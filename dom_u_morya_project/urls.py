"""dom_u_morya_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# static отвечает за обработку статических файлов
from django.conf.urls.static import static
from django.conf import settings  # доступ к модулю settings.py
from houses.views import houses_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", houses_list)  # path - связывает адресс страницы с представлением, " " - пустая строка (url путь главной страницы), houses_list - функция представления из файла urls.py
]

# связывание URL медиа  в браузере с медиа на жестком диске, отдавать как есть
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
