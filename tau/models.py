from django.db import models
from users.models import Department

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    roll = models.IntegerField()
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email  = models.EmailField(max_length=90, unique=True)
    course = models.CharField(max_length=30)
    semester = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    college = models.CharField(max_length=120)
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname
    
    
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    teacher = models.IntegerField()
    course = models.CharField(max_length=30)
    semester = models.IntegerField()
    subject = models.CharField(max_length=30)
    students = models.ManyToManyField(Student)
    attendance = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)    
    def __str__(self):
        return str(self.id)
