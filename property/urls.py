from django.urls import path,include
from .views import properties

urlpatterns = [
     path('get_property', properties, name="properties"),
   

]