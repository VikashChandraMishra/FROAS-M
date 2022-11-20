from django.db import models
    
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    
         
    def __str__(self):
        return self.name
        

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email  = models.EmailField(max_length=90, unique=True, default="teacher@gmail.com")
    password = models.CharField(max_length=200, default="to be input")
    subject1 = models.CharField(max_length=20, default="to be input")
    subject2 = models.CharField(max_length=20, default="NA")
    subject3 = models.CharField(max_length=20, default="NA")
    subject4 = models.CharField(max_length=20, default="NA")    
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    college = models.CharField(max_length=120, default="to be input")
    
         
    def __str__(self):
        return self.firstname + self.lastname
    