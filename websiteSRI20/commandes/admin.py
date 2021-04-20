from django.contrib import admin
from .models import Commande

# Register your models here.
class CommandeAdmin(admin.ModelAdmin):
    list_display = ('id','client','article','date_creation')
admin.site.register(Commande,CommandeAdmin)
