from django.contrib import admin

from .models import Purchasesdaybook

class Purchases(admin.ModelAdmin):
        list_display = ('date','details','invoicenumber','amount',)
        list_filter = ('date','details','invoicenumber','amount')

admin.site.register(Purchasesdaybook,Purchases)
