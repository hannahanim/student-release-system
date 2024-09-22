from django.db import models

# Create your models here.

class Mentor(models.Model):
    mentor_id = models.CharField(primary_key=True, max_length=10)
    mentor_name = models.TextField(max_length=100)
    mentor_department = models.TextField(max_length=20)  
    experiences = models.IntegerField(null=True, blank=True)
    mentor_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100)
    passwordmentor = models.CharField(max_length=20, default="mentorkpmb@2024")

class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=10)
    mentor_id = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student_name = models.TextField(max_length=100)
    class_stud = models.CharField(max_length=7) 
    program = models.TextField(max_length=100)
    student_number = models.CharField(max_length=20, null=True, blank=True)
    parent_name = models.TextField(max_length=100)
    parent_number = models.CharField(max_length=20, null=True, blank=True)
    parent_adress = models.TextField(max_length=200)
    passwordstud = models.CharField(max_length=25, default="studentkpmb@2024")

class Administrator(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=10)
    admin_name = models.TextField(max_length=100)
    admin_department = models.TextField(max_length=20)
    admin_number = models.CharField(max_length=20, null=True, blank=True)
    passwordadmin = models.CharField(max_length=20, default="adminkpmb@2024")

class Application(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_finish = models.DateField()
    total_leave = models.IntegerField(null=True, blank=True)
    reason = models.TextField(max_length=200)
    place = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default="Pending") 
    classestobemissed = models.CharField(max_length=20, null=True, blank=True)
