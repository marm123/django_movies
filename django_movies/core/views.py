# from django.http import HttpResponse
# from django import views
# from django.views.generic import TemplateView
import logging
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView

from core.models import Movie, AGE_LIMIT_CHOICES
from core.forms import MovieForm

LOGGER = logging.getLogger(__name__)


class MovieCreateView(CreateView):
    title = 'Add Movie'
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('index')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=None, **kwargs)
        context['limits'] = AGE_LIMIT_CHOICES
        return context


# class MovieView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {
#         'movies': Movie.objects.all(),
#         'limits': AGE_LIMIT_CHOICES
#     }

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
