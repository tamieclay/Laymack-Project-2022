from django.db import models




          

class Author(models.Model):
           name = models.CharField(max_length=200)
           email = models.EmailField()

           def __str__(self):
             return self.name

           class Meta:
            verbose_name = ('Author')
            verbose_name_plural = ('Author')


class Article(models.Model):
          
          headline = models.CharField(max_length=255)
          body_text = models.TextField()
          context=models.ImageField()
          pub_date = models.DateField()
          mod_date = models.DateField()
          authors = models.ManyToManyField(Author)

          class Meta:
           verbose_name = ('Articles')
           verbose_name_plural = ('Articles')
   

          def __str__(self):
           return self.headline


           

class Facebook(models.Model):
          
          headline = models.CharField(max_length=255)
          body_text = models.TextField()
          pub_date = models.DateField()
          mod_date = models.DateField()
          authors = models.ManyToManyField(Author)

          class Meta:
           verbose_name = ('Facebook')
           verbose_name_plural = ('Facebook')
   

          def __str__(self):
           return self.headline

       

class Twitter(models.Model):
      
       headline = models.CharField(max_length=255)
       body_text = models.TextField()
       pub_date = models.DateField()
       mod_date = models.DateField()
       authors = models.ManyToManyField(Author)
   

       def __str__(self):
        return self.headline


       class Meta:
        verbose_name = ('Twitter')
        verbose_name_plural = ('Twitter')

class Linkedin(models.Model):
       
        headline = models.CharField(max_length=255)
        body_text = models.TextField()
        pub_date = models.DateField()
        mod_date = models.DateField()
        authors = models.ManyToManyField(Author)
   

        def __str__(self):
         return self.headline


        class Meta:
         verbose_name = ('Linkedin')
         verbose_name_plural = ('Linkedin')