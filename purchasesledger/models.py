from django.db import models




class PurchasesLedger(models.Model):
        date=models.DateField()
        suppliername=models.CharField(max_length=350)
        materialparticulars=models.CharField(max_length=350)
        invoicedate=models.DateField()
        accountpayable=models.DecimalField(max_digits=9, decimal_places=2)
        inventory=models.DecimalField(max_digits=9, decimal_places=2)

        def __str__(self):
             return self.suppliername
   
        class Meta:
          verbose_name = ('PurchasesLedger')
          verbose_name_plural = ('PurchasesLedger')

