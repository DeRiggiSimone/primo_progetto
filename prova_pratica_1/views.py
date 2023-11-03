from django.shortcuts import render, random

# Create your views here.

def indexp(request):
    return render(request, "indexp.html")

def maxmin(request):
     context ={
        'var1' : random.randint(1, 10),
        'var2' : random.randint(1, 10),
    }
     return render(request, "maxmin.html")

def media(request):
    context ={
        'lista' : [random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10)],
        
    }
    return render(request, "media.html")

def voti(request):
    context ={
        'voti' : [random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10),random.randint(1, 10)],
        
    }
    return render(request, "voti.html")
