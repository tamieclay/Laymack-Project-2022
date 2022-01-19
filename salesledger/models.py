from django.db import models




class SalesLedger(models.Model):
        date=models.DateField()
        invoice=models.IntegerField()
        amount=models.DecimalField(max_digits=9, decimal_places=2)
        date=models.DateField()
        detail=models.CharField(max_length=500)
        balance=models.DecimalField(max_digits=9, decimal_places=2)

        def __str__(self):
             return self.invoice
   
        class Meta:
          verbose_name = ('SalesLedger')
          verbose_name_plural = ('SalesLedger')
