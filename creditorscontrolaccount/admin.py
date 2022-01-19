from django.contrib import admin

from .models import creditorscontrolaccount


class Filter(admin.ModelAdmin):
        list_display = ('date','number','narration','number','balance','amount')
        list_filter = ('date','number','narration','number','balance','amount')




admin.site.register(creditorscontrolaccount,Filter)
