from django.db import models

class Pettycashbook(models.Model):
        date = models.DateTimeField()
        cashathand= models.DecimalField(max_digits=9, decimal_places=2)
        item=models.CharField(max_length=255)
        invoicenumber = models.IntegerField()
        amount = models.DecimalField(max_digits=9, decimal_places=2)


        def __str__(self):
              return str(self.item)
   
        class Meta:
              verbose_name = ('Pettycashbook')
              verbose_name_plural = ('Pettycashbook')

