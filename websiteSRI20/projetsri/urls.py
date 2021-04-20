from . import views
from django.urls import path

urlpatterns=[
    path('',views.index, name="projetsri"),
    path('admin', views.AdminUser,name="admin")

]