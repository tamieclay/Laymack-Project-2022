from django.db import models


class ExpenseAccount(models.Model):
            month=models.DateTimeField()
            expenditure=models.CharField(max_length=350)
            amount = models.DecimalField(max_digits=9, decimal_places=2)


            def __str__(self):
              return str(self.expenditure)
   
            class Meta:
              verbose_name = ('ExpenseAccount')
              verbose_name_plural = ('ExpenseAccount')
