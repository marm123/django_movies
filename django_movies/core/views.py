# from django.http import HttpResponse
from django.shortcuts import render
from django import views
from django.views.generic import TemplateView

from core.models import Movie, AGE_LIMIT_CHOICES


class MovieView(TemplateView):
    template_name = 'movies.html'
    extra_context = {
        'movies': Movie.objects.all(),
        'limits': AGE_LIMIT_CHOICES
    }

# class MovieView(views.View):
#     def get(self, request):
#         return render(
#             request,
#             template_name='movies.html',
#             context={
#                 'movies': Movie.objects.all(),
#                 'limits': AGE_LIMIT_CHOICES
#             },
#         )


def hello(request):
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beautiful', 'cruel', 'wonderful']}
    )

# def hello(request):
#     return HttpResponse('Hello World!')
