# Using django module and use the view.py in this directory
from django.urls import path
from . import views 

urlpatterns = [
    # '' means supplied when unspecific situation
    path('', views.index, name="index"),
]
