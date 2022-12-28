from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def lucky(request):
    return HttpResponse('<h1>Hi!! This is Lucky</h1>')

def arpita(request):
    return HttpResponse('<h1>Hi!! This is Arpita</h1>')
