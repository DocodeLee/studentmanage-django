from django.shortcuts import render
from .models import Student

# Create your views here. function base view
def index(request):
    return render(request, 'students/index.html',{
    'students':Student.objects.all()})

