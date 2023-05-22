from django.shortcuts import render, redirect
from item.models import *
from .forms import SignupForm

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False)[0:9]
    categories = Category.objects.all()
    context = {
        'items': items,
        'categories': categories,
    }

    return render (request, 'core/index.html', context)

def contact(request):
    return render (request, 'core/contact.html') 

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form =  SignupForm()

    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context)