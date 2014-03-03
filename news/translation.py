from modeltranslation.translator import translator, TranslationOptions
from news.models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('seo_title', 'seo_description', 'seo_keywords', 'title', 'slug', 'description', 'abstract')
    empty_values = {'slug': ''}
translator.register(News, NewsTranslationOptions)