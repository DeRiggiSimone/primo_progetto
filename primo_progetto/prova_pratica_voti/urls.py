from django.urls import path
from seconda_app.views import voti_a,voti_b,voti_c,voti_d

app_name="seconda_app"
urlpatterns=[
    path('voti_a',voti_a,name='voti_a'),
    path('voti_b',voti_b,name='voti_b'),
    path('voti_c',voti_c,name='voti_c'),
    path('voti_d',voti_d,name='voti_d')
]