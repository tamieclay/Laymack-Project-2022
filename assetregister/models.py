from django.db import models

class Assetsregister(models.Model):
    date = models.DateField()
    item = models.CharField(max_length=255)
    value= models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
              return str(self.item)
   
    class Meta:
              verbose_name = ('Assets Register')
              verbose_name_plural = ('Assets Register')
