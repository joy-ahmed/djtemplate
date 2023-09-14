from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def todolist(request):
    return render(request, 'todolist.html')

def contact(request):
    return render(request, 'contact.html')


