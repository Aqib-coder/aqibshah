from django.contrib import admin
from clients.models import Client
# Register your models here.

class ClientAdmin(admin.ModelAdmin):
    list_display=("client_name","client_phone","client_email","client_work")

admin.site.register(Client,ClientAdmin)