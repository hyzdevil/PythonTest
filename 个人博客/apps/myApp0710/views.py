from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'myApp0710/index.html')

def about(request):
    return render(request, 'myApp0710/about.html')

def listpic(request):
    return render(request, 'myApp0710/listpic.html')

def newslistpic(request):
    return render(request, 'myApp0710/newslistpic.html')