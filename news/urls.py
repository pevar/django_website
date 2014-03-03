from django.conf.urls import patterns, url
from news.views import NewsList, NewsDetail

urlpatterns = patterns('',
                       url(r'^$', NewsList.as_view(), name='list'),
                       url(r'^(?P<slug>[\w+-]*)/$', NewsDetail.as_view(), name='detail'),
)