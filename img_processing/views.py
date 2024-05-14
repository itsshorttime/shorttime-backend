from django.shortcuts import render

# Create your views here.
def img_processing(request):
    return render(
        request,
        'img_processing/img_processing.html',
    )
