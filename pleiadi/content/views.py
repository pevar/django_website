from django.views.generic import ListView
from news.models import News
from pleiadi.seo.views import SeoDetailView


class BaseContentViewMixin(object):
    queryset = News.visible_on_site.all()


class BaseContentDetailView(BaseContentViewMixin, SeoDetailView):
    pass


class BaseContentListView(BaseContentViewMixin, ListView):
    pass