from django.db import models


class creditorscontrolaccount(models.Model):
    date = models.DateField()
    number = models.IntegerField()
    narration=models.CharField(max_length=250)
    date = models.DateField()
    number = models.IntegerField()
    balance = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
              return str(self.narration)
   
    class Meta:
              verbose_name = ('creditorscontrolaccount')
              verbose_name_plural = ('creditorscontrolaccount')
