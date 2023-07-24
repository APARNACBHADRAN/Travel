from django.shortcuts import render
from .models import place, upcoming


# Create your views here.
def demo(request) :
    obj=place.objects.all()
    ob=upcoming.objects.all()
    return render(request,"index.html",{'result':obj,'res':ob})

