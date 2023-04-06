from django.http import HttpResponse
# from django.shortcuts import render


def home(request):
    return HttpResponse('<html><body>Olá Django</body></html>', content_type='text/html')
