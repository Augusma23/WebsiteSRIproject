from . import views
from django.urls import path

urlpatterns=[
    path('',views.list_clients,name="clients")
]