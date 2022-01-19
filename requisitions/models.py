from django.db import models


class Requisition(models.Model):
      service = models.CharField(max_length=150)
      date = models.DateField()
      purpose = models.CharField(max_length=300)
      amount= models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
      preparedby = models.CharField(max_length=100)
      quotation1=models.ImageField()
      quotation2=models.ImageField()
      quotation3=models.ImageField()
      

      def __str__(self):
        return self.purpose


      class Meta:
        verbose_name = ('Requisition')
        verbose_name_plural = ('Requisition')



status_choice = (('approved','APPROVED'),('pending','PENDING'),('rejected','REJECTED'))


class Review(models.Model):
    id=models.CharField(primary_key=True,max_length=100)
    status= models.CharField(max_length=10,choices=status_choice,default='pending')
    budget=models.ForeignKey(Requisition, on_delete=models.CASCADE)
    comment=models.CharField(max_length=150)

    def __str__(self):
     return str(self.status)
   
    class Meta:
        verbose_name = ('Review')
        verbose_name_plural = ('Review')
