from django.db import models



class Foundation(models.Model):
    job=models.CharField(max_length=150)
    material=models.CharField(max_length=150)
    cost=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    labour=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    @property
    def total(self):
            if(self.cost != None ):
                total = self.cost + self.labour
                return total
    
    def __str__(self):
        return self.job


    class Meta:
        verbose_name = ('Foundation')
        verbose_name_plural = ('Foundation')


class Superstructure(models.Model):
       job=models.CharField(max_length=150)
       material=models.CharField(max_length=150)
       cost=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
       labour=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

       def __str__(self):
        return self.job


       class Meta:
        verbose_name = ('Superstructure')
        verbose_name_plural = ('Superstructure')



class Roofing(models.Model):
    job=models.CharField(max_length=150)
    material=models.CharField(max_length=150)
    cost=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    labour=models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.job


    class Meta:
        verbose_name = ('Roofing')
        verbose_name_plural = ('Roofing')

       




    
class Service(models.Model):
        preparedby=models.CharField(max_length=150)
        service=models.TextField()
        schedule=models.DateTimeField()

        def __str__(self):
         return str(self.service)







class BillOfQuantity(models.Model):
        customer = models.CharField(max_length=100)
        superstructure = models.ForeignKey(Superstructure, on_delete=models.CASCADE)
        roofing = models.ForeignKey(Roofing, on_delete=models.CASCADE)
        foundation = models.ForeignKey(Foundation , on_delete=models.CASCADE)
        customer_email = models.EmailField(null=True, blank=True)
        billing_address = models.TextField(null=True, blank=True)
        date = models.DateField()
        valid_date = models.DateField(null=True, blank=True)
        status = models.BooleanField(default=False)


        def __str__(self):
              return str(self.customer)
    
        def get_status(self):
           return self.status

        class Meta:
          verbose_name = ('BillOfQuantity')
          verbose_name_plural = ('BillOfQuantity')

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class Job(models.Model):
             customer = models.ForeignKey(BillOfQuantity, on_delete=models.CASCADE)
             service = models.TextField()
             description = models.TextField()
             quantity = models.CharField(max_length=150)
             amount = models.DecimalField(max_digits=9, decimal_places=2)

             def __str__(self):
              return str(self.customer)
   
             class Meta:
              verbose_name = ('Job')
              verbose_name_plural = ('Job')



class Invoice(models.Model):
    customer = models.CharField(max_length=100)
    customer_email = models.EmailField(null=True, blank=True)
    billing_address = models.TextField(null=True, blank=True)
    date = models.DateField()
    due_date = models.DateField(null=True, blank=True)
    message = models.TextField(default= "this is a default message.")
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return str(self.customer)
    
    def get_status(self):
        return self.status



    def __str__(self):
        return self.customer


    class Meta:
        verbose_name = ('Invoice')
        verbose_name_plural = ('Invoice')

    # def save(self, *args, **kwargs):
        # if not self.id:             
        #     self.due_date = datetime.datetime.now()+ datetime.timedelta(days=15)
        # return super(Invoice, self).save(*args, **kwargs)

class LineItem(models.Model):
    customer = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    service = models.TextField()
    description = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.customer)


    class Meta:
        verbose_name = ('LineItem')
        verbose_name_plural = ('LineItem')
   



class Order(models.Model):
    
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country_code = models.CharField(max_length=4, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    payment_option = models.CharField(max_length=200, blank=True)
    billing_status = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    service = models.ForeignKey(Service, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

 
