from django.db import models

class Labour(models.Model):
 project=models.CharField(max_length=255)
 labourhours=models.IntegerField()
 rate=models.IntegerField()

 

 def __str__(self):
        return str(self.project)

class Meta:
              verbose_name = ('Labour')
              verbose_name_plural = ('Labour')


@property
def labour(self):
    if(self.labourhours != None):
        labour=self.labourhours * self.rate
        return labour
