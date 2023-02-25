from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'myapp/home.html',context)
