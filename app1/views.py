from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
    return HttpResponse('<h1>This is first view of app1</h1>')

def sec(request):
    return HttpResponse('<h1>This is second view of app1</h1>')