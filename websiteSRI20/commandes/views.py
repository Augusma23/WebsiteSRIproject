from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .formulaire import CommandeForm

#from django.http import HttpResponse
#from .models import Article
# Create your views here.
@login_required(login_url='acces')
def list_commandes(request):
    return render(request,'commandes/list_commandes.html')
    #article=Article.objects.all()
    #return render(request,'index.html', {'article':article})

@login_required(login_url='acces')
def FaireCommande(request):
    if request.method=="POST":
        form=CommandeForm(request.POST).save()
        return redirect('commandes')
    else:
        form=CommandeForm()
    context={'form': form}
    return render(request,'commandes/list_commandes.html',context)