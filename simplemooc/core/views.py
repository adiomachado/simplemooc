from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
    #return HttpResponse('Hello World')

def contact(request):
    return render(request,'contact.html')

def index(request):
    return redirect('/home/')