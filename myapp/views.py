from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'myapp/index.html',context)

def about(request):
    context = {}
    return render(request, 'myapp/about.html',context)

def pricing(request):
    context = {}
    return render(request, 'myapp/pricing.html',context)
