from django.shortcuts import render

# Create your views here.

def index(request):
    return render(
        request,
        'base/index.html',
    )

def about(request):
    return render(
        request,
        'base/about.html',
    )

def img_processing(request):
    return render(
        request,
        'base/img_processing.html',
    )

def img_result(request):
    return render(
        request,
        'base/img_result.html',
    )