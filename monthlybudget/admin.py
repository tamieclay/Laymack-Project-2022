from django.contrib import admin

from .models import MonthlyBudget,Review

class ReviewInline(admin.TabularInline):
    model= Review
    extra= 0

class Task(admin.ModelAdmin):
    inlines=[ReviewInline]
    list_display = ('todo', 'day', 'labourhours','rate','materials','travel','other','notes','budget','actual','undercover')


    
class RevAdmin(admin.ModelAdmin):

    list_display = ('id','status','budget','comment')
    list_filter = ('budget','status',)


admin.site.register(MonthlyBudget,Task)
admin.site.register(Review,RevAdmin)