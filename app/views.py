from django.shortcuts import render
from . models import Student
# Create your views here.
def index(request):
    hello=Student.objects.all()
    return render(request,"index.html",{"hello":hello})
