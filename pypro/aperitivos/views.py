from django.shortcuts import render
from django.urls import reverse


class Video:
    def __init__(self, slug, titulo, vimeo_id):
        self.slug = slug
        self.titulo = titulo
        self.vimeo_id = vimeo_id

    def get_absolute_url(self):
        return reverse('aperitivos:video', args=(self.slug,))


videos = [
    Video('motivacao', 'Video Aperitivo: Motivação', '816305935'),
    Video('instalacao-windows', 'Instalação do Windows', '817023152'),
    ]

videos_dct = {dct.slug: dct for dct in videos}


def video(request, slug):
    video = videos_dct[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})


def indice(request):
    return render(request, 'aperitivos/indice.html', context={'videos': videos})
