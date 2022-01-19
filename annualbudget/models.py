from django.db import models

class AnnualBudget(models.Model):
    task=models.CharField(max_length=255)
    mounth=models.DateTimeField()
    labourhours=models.IntegerField()
    rate=models.DecimalField(max_digits=9, decimal_places=2)
    materials=models.DecimalField(max_digits=9, decimal_places=2)
    travel=models.DecimalField(max_digits=9, decimal_places=2)
    other=models.DecimalField(max_digits=9, decimal_places=2)
    notes=models.CharField(max_length=450)
    budget=models.DecimalField(max_digits=9, decimal_places=2)
    actual=models.DecimalField(max_digits=9, decimal_places=2)
    undercover=models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
              return str(self.task)
   
    class Meta:
              verbose_name = ('AnnualBudget')
              verbose_name_plural = ('AnnualBudget')




status_choice = (('approved','APPROVED'),('pending','PENDING'),('rejected','REJECTED'))


class Review(models.Model):
    id=models.CharField(primary_key=True,max_length=100)
    status= models.CharField(max_length=10,choices=status_choice,default='pending')
    budget=models.ForeignKey(AnnualBudget, on_delete=models.CASCADE)
    comment=models.CharField(max_length=150)

    def __str__(self):
     return str(self.status)
   
    class Meta:
        verbose_name = ('Review')
        verbose_name_plural = ('Review')