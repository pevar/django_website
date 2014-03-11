from pleiadi.seo.translation import SeoTranslationOptions


class BaseTranslationOptions(SeoTranslationOptions):
    fields = ('title', 'slug', 'description', 'abstract', 'visible')
    empty_values = {'slug': ''}