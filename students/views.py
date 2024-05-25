#  HttpResponseRedirect is used to redirect the user's browser to a different URL.
from django.http import HttpResponseRedirect
from django.shortcuts import render
#  reverse is used to generate URLs based on view names.
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# Create your views here. function base view
def index(request):
    return render(request, 'students/index.html',{
    'students':Student.objects.all()})

def view_student(request, id):
    Student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_major = form.cleaned_data['major']
            new_gpa = form.cleaned_data['gpa']
        
            new_student = Student(
            student_number = new_student_number,
            first_name= new_first_name,
            last_name=new_last_name,
            major= new_major,
            email=new_email,
            gpa=new_gpa,
        )
        new_student.save()
        return render(request, 'students/add.html',{
            'form': StudentForm(),
            'success': True
        })
    else:
        form = StudentForm()
        return render(request, 'students/add.html',{
             'form': StudentForm(),
        })
        