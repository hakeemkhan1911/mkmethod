from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about_auther(request):
    return render(request,'about_auther.html')