from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='acces')
def index(request):
    article=Article.objects.all()
    return render(request,'produits/accueil.html', {'article':article})

def AdminUser(request):
    redirect('/admin/')