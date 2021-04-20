from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#from django.http import HttpResponse
from .models import Client
# Create your views here.
@login_required(login_url='acces')
def list_clients(request):
    client=Client.objects.all()
    return render(request,'clients/list_clients.html', {'client':client})