from django.db import models

class Client(models.Model):
    organisation=models.CharField(max_length=200)
    period=models.CharField(max_length=150)
    guardsallocated=models.IntegerField()
    income=models.DecimalField(max_digits=9, decimal_places=2)
    contract=models.CharField(max_length=150)
    supervisor=models.CharField(max_length=150)


    def __str__(self):
        return str(self.organisation)
   
    class Meta:
        verbose_name = ('Client')
        verbose_name_plural = ('Client')



class Guards(models.Model):
    fullname=models.CharField(max_length=150)
    age=models.IntegerField()
    position=models.CharField(max_length=150)
    school=models.CharField(max_length=150)
    qualifications=models.CharField(max_length=150)
    workexperience=models.IntegerField()
    profilepicture=models.ImageField()
    reference=models.CharField(max_length=250)
    phonenumber=models.IntegerField()
    address=models.CharField(max_length=300)
    email=models.EmailField()
    performanceappraisal=models.CharField(max_length=150)
    rating=models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.position)
   
    class Meta:
        verbose_name = ('Guards')
        verbose_name_plural = ('Guards')



class GuardsNeeded(models.Model):
    position=models.CharField(max_length=200)
    education=models.CharField(max_length=200)
    experience=models.CharField(max_length=200)
    duedate=models.DateField()

    def __str__(self):
        return str(self.position)
   
    class Meta:
        verbose_name = ('GuardsNeeded')
        verbose_name_plural = ('GuardsNeeded')

