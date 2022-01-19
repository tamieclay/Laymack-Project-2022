from django.contrib import admin
from .models import PurchasesLedger

class Ledger(admin.ModelAdmin):
        list_display = ('date','suppliername','materialparticulars','invoicedate','accountpayable','inventory')
        list_filter = ('date','suppliername','materialparticulars','invoicedate','accountpayable','inventory')



admin.site.register(PurchasesLedger,Ledger )
