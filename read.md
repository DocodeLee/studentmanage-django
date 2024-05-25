# pip is the library of the python
# virtual environment help control the version for each projects
# django-admin startproject django_project .  this makes file route more clear
# Under project there are apps
# each app controls an isolated functionality
# __init__.py helps to distnict

# after make model i use 'python manage.py makemigration and django gives me migration

# Django template Tag
display logig: {% if %}   {% else %}   {% endif %} 
loop control :  {% for x in y %}   {% endfor %}
Block Declaration :  {% block body %}   {% endblock %} 
Content import :  {% include "index.html" %} 
Inheritance :  {% extends "base.html" %} 

# template variabel
 covered by {{    }}
 
 #123123

 # DATA flow in djanog and all most the web
 ## DJANGO REQUEST RESPONSIVE CYCLE
 from the client browsere the request go through from web server and to the database
 from the databse throught the template response go out to the client browser   
 ## MODEL_VIEW TEMPLATE PATTERN
    data flow gothrough from django and url to view to the data and
    data comeback with template through the django

# What is Field
 Fields define the type of data that can be stored in a database column and provide various options for validation, default values, and other behaviors.