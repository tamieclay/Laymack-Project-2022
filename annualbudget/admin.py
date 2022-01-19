from django.contrib import admin

from .models import AnnualBudget,Review

class ReviewInline(admin.TabularInline):
    model= Review
    extra= 0


class Task(admin.ModelAdmin):
    inlines=[ReviewInline]
    list_display = ('task', 'mounth', 'labourhours','rate','materials','travel','other','notes','budget','actual','undercover')

class Rev(admin.ModelAdmin):
    list_display = ('id', 'status', 'budget','comment')


admin.site.register(AnnualBudget,Task)
admin.site.register(Review,Rev)