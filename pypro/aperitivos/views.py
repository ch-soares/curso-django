from django.shortcuts import render, get_object_or_404
from pypro.aperitivos.models import Video


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    videos = Video.objects.order_by('criado_em').all()
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
