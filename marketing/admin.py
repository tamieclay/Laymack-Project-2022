from django.contrib import admin


# Register your models here.
from .models import   Linkedin , Author, Twitter, Facebook,Article



admin.site.register(Facebook)
admin.site.register(Twitter)
admin.site.register(Linkedin)
admin.site.register(Author)
admin.site.register(Article)
