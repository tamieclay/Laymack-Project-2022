from django.contrib import admin
from .models import  Requisition,Review

class ReviewInline(admin.TabularInline):
    model= Review
    extra= 0


class Filter(admin.ModelAdmin):
    inlines=[ReviewInline]
    list_display = ('service','date','purpose','amount','preparedby','quotation1','quotation2','quotation3')
    list_filter = ('service','purpose')

class RevAdmin(admin.ModelAdmin):

    list_display = ('id','status','budget','comment')
    list_filter = ('budget','status',)

admin.site.register(Requisition, Filter)
admin.site.register(Review,RevAdmin)
