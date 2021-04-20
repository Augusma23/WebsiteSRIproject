from django.forms import ModelForm
from .models import Commande
from projetsri.models import Article
#from clients.models import Client
from django.db import models


class CommandeForm(ModelForm):
    class Meta:
        model= Commande
        fields= ['client','article']




