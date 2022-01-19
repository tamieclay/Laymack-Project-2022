from django.urls import path
from home import views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('labourbroking', views.labourbroking, name='labourbroking'),
    path('transport', views.transport, name='transport'),
    path('security', views.security, name='security'),
    path('construction', views.construction, name='construction'),
    path('labourbroking', views.security, name='labourbroking'),
    


]

