from django.db import models

class Suspense(models.Model):
        date=models.DateField()
        details=models.CharField(max_length=350)
        debit=models.DecimalField(max_digits=9, decimal_places=2)
        date=models.DateField()
        details=models.CharField(max_length=350)
        credit=models.DecimalField(max_digits=9, decimal_places=2)

        def __str__(self):
             return self.suppliername
   
        class Meta:
          verbose_name = ('PurchasesLedger')
          verbose_name_plural = ('PurchasesLedger')
