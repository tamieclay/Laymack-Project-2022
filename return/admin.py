from django.contrib import admin

from .models import Labour



class Task(admin.ModelAdmin):
    list_display = ('project', 'labourhours', 'rate',)

admin.site.register(Labour,Task)
