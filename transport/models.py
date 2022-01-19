from django.db import models

class Drivers(models.Model):
   name=models.CharField(max_length=150)
   age=models.IntegerField()
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
        return str(self.name)
   
class Meta:
        verbose_name = ('Drivers')
        verbose_name_plural = ('Drivers')


class InternMechanics(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()
    job=models.CharField(max_length=150)
    school=models.CharField(max_length=150)
    profilepicture=models.ImageField()
    reference=models.CharField(max_length=250)
    phonenumber=models.IntegerField()
    address=models.CharField(max_length=300)
    email=models.EmailField()
    performanceappraisal=models.CharField(max_length=150)
    rating=models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.name)
   
    class Meta:
        verbose_name = ('InternMechanics')
        verbose_name_plural = ('InternMechanics')



class Mechanic(models.Model):
   name=models.CharField(max_length=150)
   age=models.IntegerField()
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
      return str(self.name)
   
   class Meta:
     verbose_name = ('Mechanics')
     verbose_name_plural = ('Mechanics')














class Routes(models.Model):
             truckreg = models.CharField(max_length=100)
             date = models.DateTimeField()
             driversname = models.CharField(max_length=100)
             costcentre = models.CharField(max_length=100)
             destinationname = models.CharField(max_length=100)
             orderid = models.DecimalField(max_digits=9, decimal_places=2)
             timeout = models.TimeField()
             timein = models.TimeField()
             openingkms=models.CharField(max_length=100)
             closingkms=models.CharField(max_length=100)
             distance=models.CharField(max_length=100)
             litres=models.CharField(max_length=100)
             priceperlitre = models.DecimalField(max_digits=9, decimal_places=2)

             def __str__(self):
              return str(self.destinationname)
   
             class Meta:
              verbose_name = ('Routes')
              verbose_name_plural = ('Routes')


class Bagsbyo(models.Model):
     destination = models.CharField(max_length=100)
     destinationcode=models.IntegerField()
     distance=models.IntegerField()
     usdrate = models.DecimalField(max_digits=9, decimal_places=2)
     rtgsrate = models.DecimalField(max_digits=9, decimal_places=2)

            
     def __str__(self):
        return str(self.destination)
   
     class Meta:
        verbose_name = ('Bagsbyo')
        verbose_name_plural = ('Bagsbyo')

class Bagshre(models.Model):
     destination = models.CharField(max_length=100)
     destinationcode=models.IntegerField()
     distance=models.IntegerField()
     usdrate = models.DecimalField(max_digits=9, decimal_places=2)
     rtgsrate = models.DecimalField(max_digits=9, decimal_places=2)

            
     def __str__(self):
        return str(self.destination)
   
     class Meta:
        verbose_name = ('Bagshre')
        verbose_name_plural = ('Bagshre')


class Bulkbyo(models.Model):
     destination = models.CharField(max_length=100)
     destinationcode=models.IntegerField()
     distance=models.IntegerField()
     usdrateperton = models.DecimalField(max_digits=9, decimal_places=2)
     rtgsrateperton = models.DecimalField(max_digits=9, decimal_places=2)

            
     def __str__(self):
        return str(self.destination)
   
     class Meta:
        verbose_name = ('Bulkbyo')
        verbose_name_plural = ('Bulkbyo')


class Bulkhre(models.Model):
     destination = models.CharField(max_length=100)
     destinationcode=models.IntegerField()
     distance=models.IntegerField()
     usdrateperton = models.DecimalField(max_digits=9, decimal_places=2)
     rtgsrateperton = models.DecimalField(max_digits=9, decimal_places=2)

            
     def __str__(self):
        return str(self.destination)
   
     class Meta:
        verbose_name = ('Bulkhre')
        verbose_name_plural = ('Bulkhre')


class Trip(models.Model):
      status = models.CharField(max_length=100)
      region = models.CharField(max_length=100)
      origincountry= models.CharField(max_length=100)
      destinationname = models.CharField(max_length=100)
      destinationcountry = models.CharField(max_length=100)
      origincode=models.CharField(max_length=100)
      tripcode=models.CharField(max_length=100)
      ppcso=models.CharField(max_length=100)
      deliverynote=models.IntegerField()
      currency=models.CharField(max_length=100)
      shippingdate = models.TimeField()
      planneddeliverydate = models.TimeField()
      planneddeliveryday = models.TimeField()
      planneddistance = models.TimeField()
      currency=models.CharField(max_length=100)
      shipping=models.DateField()
      planneddelivery=models.DateField()
      planneddistance=models.CharField(max_length=100)
      realproductclass=models.CharField(max_length=100)
      cpk = models.DecimalField(max_digits=9, decimal_places=2)
      vatpercentage = models.DecimalField(max_digits=9, decimal_places=2)
      variablecost = models.DecimalField(max_digits=9, decimal_places=2)
      fixedcost = models.DecimalField(max_digits=9, decimal_places=2)
      vatamount= models.DecimalField(max_digits=9, decimal_places=2)

      def __str__(self):
         return str(self.destinationname)
   
      class Meta:
         verbose_name = ('Trip')
         verbose_name_plural = ('Trip')



         
class Fixedcost(models.Model):
      product=models.CharField(max_length=150)
      cost=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    

      class Meta:
        verbose_name = ('Fixedcost')
        verbose_name_plural = ('Fixedcost')

class Variablekmcost(models.Model):
       product=models.CharField(max_length=150)
       cost=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

       def __str__(self):
         return self.product


       class Meta:
        verbose_name = ('Variablekmcost')
        verbose_name_plural = ('Variablekmcost')



class Ancillaries(models.Model):
    product=models.CharField(max_length=150)
    cost=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    

    def __str__(self):
        return self.product


    class Meta:
        verbose_name = ('Ancillaries')
        verbose_name_plural = ('Ancillaries')