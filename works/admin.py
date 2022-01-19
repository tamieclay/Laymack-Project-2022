from django.contrib import admin
from .models import Projects


class Task(admin.ModelAdmin):
    list_display = ('name', 'site', 'description','view')

admin.site.register(Projects,Task)
