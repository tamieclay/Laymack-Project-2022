from django.contrib import admin
from .models import Bulkhre,Bulkbyo,Routes,Bagshre,Bagsbyo, Ancillaries,Variablekmcost,Fixedcost,Trip,Drivers,InternMechanics,Mechanic

class Bulk(admin.ModelAdmin):
    list_display = ('destination', 'destinationcode', 'distance','usdrateperton','rtgsrateperton')

class Bulky(admin.ModelAdmin):
    list_display = ('destination', 'destinationcode', 'distance','usdrateperton','rtgsrateperton')


class Bagz(admin.ModelAdmin):
    list_display = ('destination', 'destinationcode', 'distance','usdrate','rtgsrate')


class Bag(admin.ModelAdmin):
    list_display = ('destination', 'destinationcode', 'distance','usdrate','rtgsrate')

class Routez(admin.ModelAdmin):
    list_display = ('truckreg', 'date', 'driversname','costcentre','destinationname','orderid','timeout','timein','openingkms','closingkms','distance','litres','priceperlitre')


class Tripz(admin.ModelAdmin):
    list_display = ('status', 'region', 'origincountry','destinationname','destinationcountry','origincode','tripcode','ppcso',
    'deliverynote','currency','shippingdate','planneddeliverydate','planneddistance','realproductclass','cpk','vatpercentage','variablecost','fixedcost','vatamount')

class Fixed(admin.ModelAdmin):
    list_display = ('product', 'cost' )

class Variable(admin.ModelAdmin):
    list_display = ('product', 'cost')

class Anci(admin.ModelAdmin):
    list_display = ('product', 'cost')


class Drive(admin.ModelAdmin):
    list_display = ('name', 'age', 'qualifications','workexperience',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')


class Int(admin.ModelAdmin):
    list_display = ('name', 'age', 'job','school',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')


class Mech(admin.ModelAdmin):
    list_display = ('name', 'age', 'qualifications','workexperience',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')


admin.site.register(Bulkbyo,Bulk)
admin.site.register(Bulkhre,Bulky)
admin.site.register(Bagsbyo,Bagz)
admin.site.register(Bagshre,Bag)
admin.site.register(Routes,Routez)
admin.site.register(Trip,Tripz)
admin.site.register(Fixedcost,Fixed)
admin.site.register(Variablekmcost,Variable)
admin.site.register(Ancillaries,Anci)
admin.site.register(Drivers,Drive)
admin.site.register(InternMechanics,Int)
admin.site.register(Mechanic,Mech)





class TransportAdminArea(admin.AdminSite):

    site_header = 'Transport Admin Area'

transport_site = TransportAdminArea (name='TransportAdmin')

class Bulk(admin.ModelAdmin):
    list_display = ('destination', 'destinationcode', 'distance','usdrateperton','rtgsrateperton')

class Bulky(admin.ModelAdmin):
    list_display = ('destination', 'destinationcode', 'distance','usdrateperton','rtgsrateperton')


class Bagz(admin.ModelAdmin):
    list_display = ('destination', 'destinationcode', 'distance','usdrate','rtgsrate')


class Bag(admin.ModelAdmin):
    list_display = ('destination', 'destinationcode', 'distance','usdrate','rtgsrate')

class Routez(admin.ModelAdmin):
    list_display = ('truckreg', 'date', 'driversname','costcentre','destinationname','orderid','timeout','timein','openingkms','closingkms','distance','litres','priceperlitre')


class Tripz(admin.ModelAdmin):
    list_display = ('status', 'region', 'origincountry','destinationname','destinationcountry','origincode','tripcode','ppcso',
    'deliverynote','currency','shippingdate','planneddeliverydate','planneddistance','realproductclass','cpk','vatpercentage','variablecost','fixedcost','vatamount')

class Fixed(admin.ModelAdmin):
    list_display = ('product', 'cost' )

class Variable(admin.ModelAdmin):
    list_display = ('product', 'cost')

class Anci(admin.ModelAdmin):
    list_display = ('product', 'cost')


class Drive(admin.ModelAdmin):
    list_display = ('name', 'age', 'qualifications','workexperience',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')


class Int(admin.ModelAdmin):
    list_display = ('name', 'age', 'job','school',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')


class Mech(admin.ModelAdmin):
    list_display = ('name', 'age', 'qualifications','workexperience',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')


transport_site.register(Bulkbyo,Bulk)
transport_site.register(Bulkhre,Bulky)
transport_site.register(Bagsbyo,Bagz)
transport_site.register(Bagshre,Bag)
transport_site.register(Routes,Routez)
transport_site.register(Trip,Tripz)
transport_site.register(Fixedcost,Fixed)
transport_site.register(Variablekmcost,Variable)
transport_site.register(Ancillaries,Anci)
transport_site.register(Drivers,Drive)
transport_site.register(InternMechanics,Int)
transport_site.register(Mechanic,Mech)

