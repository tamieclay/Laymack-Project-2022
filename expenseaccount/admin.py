from django.contrib import admin

from .models import ExpenseAccount


class Filter(admin.ModelAdmin):
        list_display = ('month','expenditure','amount',)
        list_filter = ('month','expenditure','amount')

admin.site.register(ExpenseAccount,Filter)
