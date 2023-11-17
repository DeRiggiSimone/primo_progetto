from django.contrib import admin
from django.urls import path
from news.views import path

app_name='news'

urlpattern = [
    path('admin/',admin.site.urls),
    path("", home, name="homeview")
]