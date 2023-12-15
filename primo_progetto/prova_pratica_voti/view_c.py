from django.shortcuts import render
import datetime

# Create your views here.
def voti(request):
    context ={
        'voti' : {'Giuseppe Gullo':[("Matematica",9,0),("Italiano",7,3),("Inglese",7,4),("Storia",7,4),("Geografia",5,7)],
                  'Antonio Barbera':[("Matematica",8,1),("Italiano",6,1),("Inglese",9,0),("Storia",8,2),("Geografia",8,1)],
                  'Nicola Spina':[("Matematica",7,2),("Italiano",6,2),("Inglese",4,3),("Storia",8,2),("Geografia",8,2)]}
    }
    somma=0
    for studente, dati in voti.items():
        for i in range(voti):
            somma+=voti[studente][i][1]
            media=somma/5
    print("La media di tutti i voti",media)
    return render(request, "voti_c.html", context)