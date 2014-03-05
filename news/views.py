from pleiadi.content.views import BaseContentListView, BaseContentDetailView
from news.models import News


class NewsList(BaseContentListView):
    model = News


class NewsDetail(BaseContentDetailView):
    model = News
