from django.db import models


class Status(models.Model):
    supervisor=models.CharField(max_length=150)
    date=models.DateField
    job=models.TextField(max_length=350)
    teamonsite=models.TextField()
    materialsused=models.TextField()
    site=models.ImageField()


    def __str__(self):
        return str(self.job)

    class Meta:
        verbose_name = ('Status')
        verbose_name_plural = ('Status')