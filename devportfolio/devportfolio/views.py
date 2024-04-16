from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'about/index.html')

def work(request):
    return render(request, 'work/index.html')

def contact(request):
    return render(request, 'contact/index.html')
