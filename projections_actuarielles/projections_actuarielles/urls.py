# projections_actuarielles/projections_actuarielles/urls.py 
 
from django.contrib import admin 
from django.urls import path, include

 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('', include('projections.urls')), 
] 
 
