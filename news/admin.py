from django.contrib import admin
from news.models import News
from pleiadi.content.admin import BaseContentAdmin


class NewsAdmin(BaseContentAdmin):
    pass

admin.site.register(News, NewsAdmin)