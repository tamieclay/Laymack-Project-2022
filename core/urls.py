"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from transport.admin import transport_site
from construction.admin import construction_site
from labourbroking.admin import labourbroking_site
from security.admin import security_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('transportadmin/', transport_site.urls),
    path('constructionadmin/', construction_site.urls),
     path('labourbrokingadmin/', labourbroking_site.urls),
     path('securityadmin/', security_site.urls),
     path('',  include ('home.urls')),
 
    
     
     
]


urlpatterns =urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  




admin.site.index_title = 'Laymack '

admin.site.site_header = 'Laymack  Admin'

admin.site.site_title = 'Laymark'