from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.
def subscribe(request):
    return render(request, 'Subscribe.html')
def login(request):
    return render(request, 'Login.html')