from django.shortcuts import render
import datetime

# Create your views here.
def voti(request):
    context ={
       'materie' : ["Matematica","Italiano","Inglese","Storia","Geografia"]
    }
    return render(request, "voti_a.html", context)