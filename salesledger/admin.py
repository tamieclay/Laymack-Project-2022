from django.contrib import admin
from .models import SalesLedger

class Ledger(admin.ModelAdmin):
        list_display = ('date','invoice','amount','date','detail','balance')
        list_filter = ('date','invoice','amount','date','detail','balance')



admin.site.register(SalesLedger,Ledger )

