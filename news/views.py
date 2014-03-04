from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from pleiadi.content.views import BaseDetailView
from news.models import News


class NewsList(ListView):
    model = News


class NewsDetail(BaseDetailView):
    model = News
