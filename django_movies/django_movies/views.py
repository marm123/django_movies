from django_movies.core.views import MovieListView


class IndexView(MovieListView):
    template_name = 'index.html'
