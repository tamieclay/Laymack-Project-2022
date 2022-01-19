from django.contrib import admin

from .models import Assetsregister


class Assets(admin.ModelAdmin):
        list_display = ('date','item','value',)
        list_filter = ('date','item','value')

   

admin.site.register(Assetsregister,Assets)