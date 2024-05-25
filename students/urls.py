# Using django module and use the view.py in this directory
from django.urls import path
from . import views 

urlpatterns = [
    # '' means supplied when unspecific situation
    path('', views.index, name="index"),
    # captures an integer ID from the URL and passes it to the view_student function
    path('<int:id>', views.view_student, name='view_student'),
    path('add/',views.add, name="add"),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
