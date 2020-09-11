from django.shortcuts import render
# from django.http import HttpResponse
from django.shortcuts import render

from core.models import Movie


def hello(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beautiful', 'cruel', 'wonderful']}
    )

# def hello(request):
#     return HttpResponse('Hello World!')
