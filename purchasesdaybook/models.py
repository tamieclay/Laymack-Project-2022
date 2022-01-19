from django.db import models

class Purchasesdaybook(models.Model):
        date = models.DateField()
        details=models.TextField()
        invoicenumber=models.IntegerField()
        amount = models.DecimalField(max_digits=9, decimal_places=2)

        def __str__(self):
              return str(self.details)
   
        class Meta:
              verbose_name = ('Purchasesdaybook')
              verbose_name_plural = ('Purchasesdaybook')
