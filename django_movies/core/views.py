# from django.http import HttpResponse
# from django.views.generic import TemplateView
import logging
from django import views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, CreateView, UpdateView, DeleteView, DetailView

from core.models import Movie, AGE_LIMIT_CHOICES
from core.forms import MovieForm

logging.basicConfig(
    filename='log.txt',
    filemode='w',
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'form.html'
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def post(self, request, *args, **kwargs):
        LOGGER.info(f"Added new movie: {self.request.POST['title']}")
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)


class MovieUpdateView(StaffRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = 'form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('core:movie_list')

    def form_invalid(self, form):
        LOGGER.warning('Invalid data provided.')
        return super().form_invalid(form)

    def test_func(self):
        super().test_func()
        return self.request.user.is_superuser


class MovieDeleteView(StaffRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = 'movie_confirm_delete.html'
    model = Movie
    success_url = reverse_lazy('core:movie_list')


class MovieListView(ListView):
    template_name = 'movie_list.html'
    model = Movie


class MovieDetailView(DetailView):
    template_name = 'movie_detail.html'
    model = Movie




# class MovieView(ListView):
#     template_name = 'movies.html'
#     model = Movie
#
#     def get_context_data(self, *args, object_list=None, **kwargs):
#         context = super().get_context_data(*args, object_list=None, **kwargs)
#         context['limits'] = AGE_LIMIT_CHOICES
#         return context

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
    LOGGER.info('\nWreszcie cos dziala\n')
    return render(
        request,
        template_name='hello.html',
        context={'adjectives': ['beautiful', 'cruel', 'wonderful']}
    )

# def hello(request):
#     return HttpResponse('Hello World!')
