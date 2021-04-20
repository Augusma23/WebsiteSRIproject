from django.db import models
from clients.models import Client
from projetsri.models import Article

# Create your models here.
class Commande(models.Model):
    client=models.ForeignKey (Client,null=True,on_delete=models.SET_NULL)
    article=models.ForeignKey(Article,null=True,on_delete=models.SET_NULL)
    date_creation=models.DateTimeField(auto_now_add=True, null=True)
