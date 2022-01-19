from django.contrib import admin

from .models import Salesdaybook

class Sales(admin.ModelAdmin):
        list_display = ('date','particulars','amount','invoicenumber',)
        list_filter = ('date','particulars','amount','invoicenumber')

admin.site.register(Salesdaybook,Sales)
