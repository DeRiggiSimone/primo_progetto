from django.urls import path,maxmin,media,voti
from .views import home

app_name= 'prova_pratica_1'
urlpatterns=[
    path('maxmin',maxmin,name='maxmin'),
    path('media',media,name='media'),
    path('voti',voti,name='voti')
]