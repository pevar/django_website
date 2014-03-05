from pleiadi.content.translation import BaseTranslationOptions
from modeltranslation.translator import translator
from news.models import News


class NewsTranslationOptions(BaseTranslationOptions):
    pass

translator.register(News, NewsTranslationOptions)