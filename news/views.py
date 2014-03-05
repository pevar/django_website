from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from pleiadi.content.views import BaseDetailView
from news.models import News


class NewsList(ListView):
    model = News
    queryset = News.active_on_site.all()


class NewsDetail(BaseDetailView):
    model = News
