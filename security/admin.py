from django.contrib import admin
from .models import Client,Guards,GuardsNeeded

class Clientz(admin.ModelAdmin):
    list_display = ('organisation', 'period', 'guardsallocated','income','contract','supervisor')

class Guardz(admin.ModelAdmin):
    list_display = ('fullname', 'age', 'position','school','qualifications','workexperience',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')


class GuardsNid(admin.ModelAdmin):
    list_display = ('position', 'education', 'experience','duedate')


admin.site.register(Client,Clientz)
admin.site.register(Guards,Guardz)
admin.site.register(GuardsNeeded,GuardsNid)


class SecurityAdminArea(admin.AdminSite):

    site_header = 'Security Admin Area'

security_site = SecurityAdminArea (name='SecurityAdmin')

class Clientz(admin.ModelAdmin):
    list_display = ('organisation', 'period', 'guardsallocated','income','contract','supervisor')

class Guardz(admin.ModelAdmin):
    list_display = ('fullname', 'age', 'position','school','qualifications','workexperience',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')


class GuardsNid(admin.ModelAdmin):
    list_display = ('position', 'education', 'experience','duedate')


security_site.register(Client,Clientz)
security_site.register(Guards,Guardz)
security_site.register(GuardsNeeded,GuardsNid)