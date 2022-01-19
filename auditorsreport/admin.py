from django.contrib import admin


from .models import AuditReport


class Audit(admin.ModelAdmin):
        list_display = ('departmentname','location','address','subjectofaudit','auditdate','report')
        list_filter = ('departmentname','subjectofaudit','report')

   

admin.site.register(AuditReport,Audit)
