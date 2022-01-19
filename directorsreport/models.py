from django.db import models

class InstructionManualConstruction(models.Model):
    title=models.CharField(max_length=255)
    requirement=models.TextField()
    expectedoutcome=models.CharField(max_length=255)
    expectedcompletion=models.DateTimeField()

    def __str__(self):
     return str(self.title)
   
class Meta:
    verbose_name = ('InstructionManual')
    verbose_name_plural = ('InstructionManual')


class InstructionManualTransport(models.Model):
    title=models.CharField(max_length=255)
    requirement=models.TextField()
    expectedoutcome=models.CharField(max_length=255)
    expectedcompletion=models.DateTimeField()

    def __str__(self):
     return str(self.title)
   
class Meta:
    verbose_name = ('InstructionManualTransport')
    verbose_name_plural = ('InstructionManualTransport')


class InstructionManualLabourbroking(models.Model):
    title=models.CharField(max_length=255)
    requirement=models.TextField()
    expectedoutcome=models.CharField(max_length=255)
    expectedcompletion=models.DateTimeField()

    def __str__(self):
     return str(self.title)
   
class Meta:
    verbose_name = ('InstructionManualLabourbroking')
    verbose_name_plural = ('InstructionManualLabourbroking')

class InstructionManualSecurity(models.Model):
    title=models.CharField(max_length=255)
    requirement=models.TextField()
    expectedoutcome=models.CharField(max_length=255)
    expectedcompletion=models.DateTimeField()

    def __str__(self):
     return str(self.title)
   
class Meta:
    verbose_name = ('InstructionManualSecurity')
    verbose_name_plural = ('InstructionManualSecurity')