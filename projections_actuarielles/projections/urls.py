# projections_actuarielles/projections/urls.py 
 
from django.urls import path 
from projections.views import liste_projections 
 
urlpatterns = [ 
    path('', liste_projections, name='liste_projections'), 
] 