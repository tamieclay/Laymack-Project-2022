from django.contrib import admin
from .models import Suspense

class Ledger(admin.ModelAdmin):
        list_display = ('date','details','debit','date','details','credit')
        list_filter = ('date','details','debit','date','details','credit')



admin.site.register(Suspense,Ledger )
