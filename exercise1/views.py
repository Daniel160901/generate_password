from django.http.response import HttpResponse
from django.shortcuts import render
import random

def home(request):
    return render(request,'exercise1/home.html',{'nombre':'Daniel Alcocer'})

def other(request):
    return HttpResponse('<h1>This is the other page</h1>')

def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('Special'):
        characters.extend(list('!"@#$%&/()=?¡¿'))
    length = int(request.GET.get('length', 8))
    pswd = ''
    for x in range(length):
        pswd += random.choice(characters)
    return render(request, 'exercise1/password.html',{'password':pswd})