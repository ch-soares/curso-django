from django.shortcuts import render, get_object_or_404
from pypro.aperitivos.models import Video


videos = [
    Video(slug='motivacao', titulo='Video Aperitivo: Motivação', vimeo_id='816305935'),
    Video(slug='instalacao-windows', titulo='Instalação do Windows', vimeo_id='817023152'),
    ]


videos_dct = {dct.slug: dct for dct in videos}


def video(request, slug):
    video = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
