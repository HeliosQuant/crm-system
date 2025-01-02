from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.

def home_page(request):
    #return render(request, "leads/home_page.html") # that's an option
    context = {
        'name': 'Joe',
        'age': 30
    }
    return render(request, 'second_page.html', context)