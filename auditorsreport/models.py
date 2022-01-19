from django.db import models

class AuditReport(models.Model):
    departmentname=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    address=models.CharField(max_length=255)
    subjectofaudit=models.CharField(max_length=255)
    auditdate=models.DateTimeField()
    report=models.TextField()

    def __str__(self):
              return str(self.departmentname)
   
    class Meta:
              verbose_name = ('AuditReport')
              verbose_name_plural = ('AuditReport')

