from django.views.generic.list import ListView
from pleiadi.content.views import BaseDetailView
from news.models import News


class NewsList(ListView):
    model = News
    queryset = News.visible_on_site.all()


class NewsDetail(BaseDetailView):
    model = News
    queryset = News.visible_on_site.all()

