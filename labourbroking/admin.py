from django.contrib import admin
from .models import Application,Jobsavailable,CurrentJobs

class Appli(admin.ModelAdmin):
    list_display = ('fullname', 'age', 'job','school','qualifications','workexperience','profilepicture','reference','phonenumber','address','email')

class Avail(admin.ModelAdmin):
    list_display = ('jobtype', 'education', 'experience','duedate')


class Current(admin.ModelAdmin):
    list_display = ('employeename', 'age', 'job','school','qualifications','workexperience',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')



admin.site.register(Application,Appli)
admin.site.register(Jobsavailable,Avail)
admin.site.register(CurrentJobs,Current)

class LabourbrokingAdminArea(admin.AdminSite):

    site_header = 'Labourbroking Admin Area'

labourbroking_site = LabourbrokingAdminArea (name='LabourbrokingAdmin')


class Appli(admin.ModelAdmin):
    list_display = ('fullname', 'age', 'job','school','qualifications','workexperience','profilepicture','reference','phonenumber','address','email')

class Avail(admin.ModelAdmin):
    list_display = ('jobtype', 'education', 'experience','duedate')


class Current(admin.ModelAdmin):
    list_display = ('employeename', 'age', 'job','school','qualifications','workexperience',
    'profilepicture','reference','phonenumber','address','email','performanceappraisal','rating')



labourbroking_site.register(Application,Appli)
labourbroking_site.register(Jobsavailable,Avail)
labourbroking_site.register(CurrentJobs,Current)