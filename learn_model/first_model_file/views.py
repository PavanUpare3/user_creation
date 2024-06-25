from django.shortcuts import render
from .models import StudentModel

def display(request):
    fm = StudentModel.objects.all()
    return render(request, 'display.html', {'model1': fm})
