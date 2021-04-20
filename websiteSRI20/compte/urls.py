from . import views
from django.urls import path

urlpatterns=[
    path('inscription',views.inscriptionPage,name="inscription"),
    path('acces', views.accesPage, name="acces"),
    path('', views.accesPage, name="acces"),
    path('quitter', views.logoutUser, name="quitter")

]
