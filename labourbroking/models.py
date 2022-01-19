from django.db import models

class Application(models.Model):
    fullname=models.CharField(max_length=150)
    age=models.IntegerField()
    job=models.CharField(max_length=150)
    school=models.CharField(max_length=150)
    qualifications=models.CharField(max_length=150)
    workexperience=models.IntegerField()
    profilepicture=models.ImageField()
    reference=models.CharField(max_length=250)
    phonenumber=models.IntegerField()
    address=models.CharField(max_length=300)
    email=models.EmailField()

    def __str__(self):
        return str(self.job)
   
    class Meta:
        verbose_name = ('Application')
        verbose_name_plural = ('Application')



class Jobsavailable(models.Model):
    jobtype=models.CharField(max_length=200)
    education=models.CharField(max_length=200)
    experience=models.CharField(max_length=200)
    duedate=models.DateField()

    def __str__(self):
        return str(self.jobtype)
   
    class Meta:
        verbose_name = ('Jobsavailable')
        verbose_name_plural = ('Jobsavailable')



class CurrentJobs(models.Model):
    employeename=models.CharField(max_length=150)
    age=models.IntegerField()
    job=models.CharField(max_length=150)
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
        return str(self.job)
   
    class Meta:
        verbose_name = ('CurrentJobs')
        verbose_name_plural = ('CurrentJobs')