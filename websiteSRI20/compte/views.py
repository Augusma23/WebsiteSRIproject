from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login, logout
from .forms import CreerUtilisateur
from django.contrib import messages


# Create your views here.
def inscriptionPage(request):
    form = CreerUtilisateur()
    if request.method=='POST':
        form=CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Votre a été enregistré avec succès comme'+user)
            return  redirect('acces')
    context={'form':form}
    return render(request,'compte/inscription.html',context)

def accesPage(request):
    context = {}
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('projetsri')
        else:
            message.info(request,"Username or password not valid")
    return render(request, 'compte/acces.html', context)

def logoutUser(request):
    logout(request)
    return redirect('acces')

