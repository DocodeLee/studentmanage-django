from django import forms
from .models import Student

#  form (StudentForm) based on the Student model. 

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'major', 'gpa' ]
        labels = {
            'student_number': 'Student Number', 
            'first_name' : 'First Name', 
            'last_name' : "Last Name", 
            'email' : "E mail", 
            'major' : 'Major' ,
            'gpa' : 'GPA',
        }
        # appearance
        widgets = {
            'student_number': forms.NumberInput(attrs={'class':'form-contorl'}),
            'first_name': forms.TextInput(attrs={'class':'form-contorl'}),
            'last_name': forms.TextInput(attrs={'class':'form-contorl'}),
            'email': forms.EmailInput(attrs={'class':'form-contorl'}), 
            'major': forms.TextInput(attrs={'class':'form-contorl'}),
            'gpa' : forms.NumberInput(attrs={'class':'form-contorl'}),
        }