from django.contrib import admin

from .models import Foundation,Superstructure,Roofing,LineItem,Order,OrderItem,Invoice,Job,BillOfQuantity,Service


class Jobz(admin.ModelAdmin):
    list_display = ('customer','service','description','quantity','amount')
    list_filter = ('customer','service',)

class Invo(admin.ModelAdmin):
    list_display = ('customer','customer_email','billing_address','date','due_date','message','total_amount','status')
    list_filter = ('customer','total_amount',)


class Line(admin.ModelAdmin):
    list_display = ('customer','service','description','quantity','rate','amount')
    list_filter = ('customer','service',)

class Serv(admin.ModelAdmin):
    list_display = ('preparedby','service','schedule')
    list_filter = ('preparedby','service',)

class Bill(admin.ModelAdmin):
    list_display = ('customer','superstructure','roofing','foundation','customer_email','billing_address','date','valid_date','status')
    list_filter = ('customer','status',)

class Fou(admin.ModelAdmin):
    list_display = ('job','material','cost','labour')
    list_filter = ('material','cost',)


class Super(admin.ModelAdmin):
    list_display = ('job','material','cost','labour')
    list_filter = ('material','cost',)


class Roof(admin.ModelAdmin):
    list_display = ('job','material','cost','labour')
    list_filter = ('material','cost',)




class Ord(admin.ModelAdmin):
    list_display = ('full_name','email','address1','address2','city','phone','postal_code','country_code','created','updated','total_paid','order_key','payment_option','billing_status')
    list_filter = ('full_name','city',)

class OrdIt(admin.ModelAdmin):
    list_display = ('order','service','price','quantity')
    list_filter = ('order','service',)



admin.site.register(Job,Jobz)
admin.site.register(Invoice,Invo)
admin.site.register(LineItem,Line)
admin.site.register(Service,Serv)
admin.site.register(BillOfQuantity,Bill)
admin.site.register(Foundation,Fou)
admin.site.register(Superstructure,Super)
admin.site.register(Roofing,Roof)
admin.site.register(Order,Ord)
admin.site.register(OrderItem,OrdIt)















class ConstructionAdminArea(admin.AdminSite):

    site_header = 'Construction Admin Area'

construction_site = ConstructionAdminArea (name='ConstructionAdmin')


class Jobz(admin.ModelAdmin):
    list_display = ('customer','service','description','quantity','amount')
    list_filter = ('customer','service',)

class Invo(admin.ModelAdmin):
    list_display = ('customer','customer_email','billing_address','date','due_date','message','total_amount','status')
    list_filter = ('customer','total_amount',)


class Line(admin.ModelAdmin):
    list_display = ('customer','service','description','quantity','rate','amount')
    list_filter = ('customer','service',)

class Serv(admin.ModelAdmin):
    list_display = ('preparedby','service','schedule')
    list_filter = ('preparedby','service',)

class Bill(admin.ModelAdmin):
    list_display = ('customer','superstructure','roofing','foundation','customer_email','billing_address','date','valid_date','status')
    list_filter = ('customer','status',)

class Fou(admin.ModelAdmin):
    list_display = ('job','material','cost','labour')
    list_filter = ('material','cost',)


class Super(admin.ModelAdmin):
    list_display = ('job','material','cost','labour')
    list_filter = ('material','cost',)


class Roof(admin.ModelAdmin):
    list_display = ('job','material','cost','labour')
    list_filter = ('material','cost',)




class Ord(admin.ModelAdmin):
    list_display = ('full_name','email','address1','address2','city','phone','postal_code','country_code','created','updated','total_paid','order_key','payment_option','billing_status')
    list_filter = ('full_name','city',)

class OrdIt(admin.ModelAdmin):
    list_display = ('order','service','price','quantity')
    list_filter = ('order','service',)



construction_site.register(Job,Jobz)
construction_site.register(Invoice,Invo)
construction_site.register(LineItem,Line)
construction_site.register(Service,Serv)
construction_site.register(BillOfQuantity,Bill)
construction_site.register(Foundation,Fou)
construction_site.register(Superstructure,Super)
construction_site.register(Roofing,Roof)
construction_site.register(Order,Ord)
construction_site.register(OrderItem,OrdIt)
