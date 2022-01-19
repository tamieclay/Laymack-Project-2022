from django.db import models

class Projects(models.Model):
    name=models.CharField(max_length=255)
    site=models.CharField(max_length=255)
    description=models.TextField()
    view=models.ImageField()

    class Meta:
        verbose_name = ('Projects')
        verbose_name_plural = ('Projects')
        


    def __str__(self):
        return self.name


