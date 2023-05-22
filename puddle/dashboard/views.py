from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item

# Create your views here.

def index(request):
    items = Item.objects.filter(created_by=request.user)
    context = {
        'items' : items
    }
    return render(request, 'dashboard/index.html', context)

