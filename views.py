#coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from pytz import timezone
from .forms import ConnectionForm
from choix_cado.models import User
from .forms import ConnectionForm, NewmdpForm
from random import *
import pytz

# Create your views here.

def home(request):
    form = ConnectionForm(None)
    date = datetime.now()
    return render(request,'choix_cado/accueil_connection.html', locals())

def connection(request):
    form = ConnectionForm(request.POST or None)
    date = datetime.now()
    if form.is_valid():
        password = form.cleaned_data['password']
        name = form.cleaned_data['name']
        # on met tout en minuscule
        password = password.lower()
        name = name.lower()
        # on remplace les é par des e et les ç par des c
        if 'é' in password:
            password = password.replace('é','e')
        if 'ç' in password:
            password = password.replace('ç','c')
        if 'é' in name:
           name = name.replace('é','e')
        # on appelle l'utilisateur qui a pour mot de passe la valeur rentrée dans la variable 'password'    
        user = User.objects.get(password=password)
        target = user.target
        return render(request,'choix_cado/destinataire.html', locals())
    return render(request,'choix_cado/accueil_connection2.html', locals())



def refresh(request):
    liste = [2,3,4,5,6,7,8,9,10,11,12,13]
    donneur=User.objects.get(id=1)
    for i in range(0,12):
        id_cible=choice(liste)
        cible=User.objects.get(id=id_cible)
        cible_name = cible.name
        if cible_name == 'stephane':
            cible_name = 'stéphane'
        elif cible_name == 'emilie':
            cible_name = 'émilie'
        elif cible_name == 'melissa':
            cible_name = 'mélissa'
        cible_name = cible_name[0].upper() + cible_name[1:]
        donneur.target=cible_name 
        liste.remove(id_cible)
        donneur.save()
        donneur=cible
    donneur.target='Timothée'
    donneur.save()
    
    return HttpResponse('Les cibles ont bien été rafraîchies')


def new_mdp(request):
    form = NewmdpForm(None)
    return render(request,'choix_cado/newmdp.html', locals())

def finalcountdown(request):
    form = NewmdpForm(request.POST or None)
    if form.is_valid():
        mdp = form.cleaned_data['newmdp']
        lastmdp = form.cleaned_data['lastmdp']
        user = User.objects.get(password=lastmdp)
        user.password = mdp
        user.save()
        return render(request,'choix_cado/finalcountdown.html')
    return render(request,'choix_cado/newmdp2.html', locals())

def lolz(request):
    return render(request,'choix_cado/lolz.html')

    
    


