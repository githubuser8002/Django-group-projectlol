from django.shortcuts import render

# Create your views here.

from .models import Student, Grade

def show_grades(request):
    students = Student.objects.all()
    grades = Grade.objects.all()
    context={
        'students': students,
        'grades': grades,
    }
    return render(request,'elec_diary/grades.html',context)

