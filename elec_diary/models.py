from django.db import models

# Create your models here.

class Student(models.Model):
    last_name = models.CharField(max_length=30)
    classes = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.last_name}, {self.classes}"
    

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=40)
    grade = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject}: {self.grade}"