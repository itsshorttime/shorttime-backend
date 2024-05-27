from django.shortcuts import render

from video.models import Video


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

def img_result(request):
    if request.method == 'POST' and request.FILES['file']:
        video_file = request.FILES['file']
        video = Video(video_file=video_file)
        video.save()
        return render(request, 'base/img_result.html', {'video_url': video.video_file.url})
    else:
        return render(request, 'error_page.html', {'message': '파일이 올바르게 전송되지 않았습니다.'})
