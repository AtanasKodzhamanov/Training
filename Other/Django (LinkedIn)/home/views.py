from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
from datetime import datetime 
from django.contrib.auth.decorators import login_required


def home(request):
    #return HttpResponse("Hellow,world")
    return render(request, "home/welcome.html",{"today": datetime.today})

@login_required
def authorized(request):
    return render(request, "home/authorized.html",{})