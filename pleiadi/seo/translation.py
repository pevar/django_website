from modeltranslation.translator import TranslationOptions


class SeoTranslationOptions(TranslationOptions):
    fields = ('seo_title', 'seo_description', 'seo_keywords',)