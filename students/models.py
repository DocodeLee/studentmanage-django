from django.db import models

# Create your models here. for database 
class Student(models.Model):
    # property which Students have
    student_number = models.PositiveIntegerField()
    # PositiveIntegerField for integar, Charfield for character data
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    major = models.CharField(max_length=50)
    gpa = models.FloatField()
    
    def __str__(self):
        return f'Student: {self.first_name} {self.last_name} {self.major}'
    