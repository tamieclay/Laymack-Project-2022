from django.contrib import admin

from .models import InstructionManualConstruction, InstructionManualSecurity, InstructionManualTransport, InstructionManualLabourbroking

class Con(admin.ModelAdmin):
    list_display = ('title', 'requirement', 'expectedoutcome','expectedcompletion')

class Secu(admin.ModelAdmin):
    list_display = ('title', 'requirement', 'expectedoutcome','expectedcompletion')

class Labour(admin.ModelAdmin):
    list_display = ('title', 'requirement', 'expectedoutcome','expectedcompletion')

class Trans(admin.ModelAdmin):
    list_display = ('title', 'requirement', 'expectedoutcome','expectedcompletion')




admin.site.register(InstructionManualConstruction,Con)
admin.site.register(InstructionManualSecurity,Secu)
admin.site.register(InstructionManualLabourbroking,Labour)
admin.site.register(InstructionManualTransport,Trans)

