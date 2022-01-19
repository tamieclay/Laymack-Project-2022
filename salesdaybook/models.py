from django.db import models

class Salesdaybook(models.Model):
    date = models.DateField()
    particulars=models.TextField()
    invoicenumber=models.IntegerField()
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
              return str(self.particulars)
   
    class Meta:
              verbose_name = ('Salesdaybook')
              verbose_name_plural = ('Salesdaybook')
