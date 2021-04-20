from . import views
from django.urls import path

urlpatterns=[
    #path('',views.list_commandes,name="commandes"),
    path('', views.FaireCommande, name="commandes")

]