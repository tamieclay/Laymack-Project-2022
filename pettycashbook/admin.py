from django.contrib import admin

from .models import Pettycashbook

class Task(admin.ModelAdmin):
    list_display = ( 'date', 'cashathand','item','invoicenumber','amount')


admin.site.register(Pettycashbook,Task)
