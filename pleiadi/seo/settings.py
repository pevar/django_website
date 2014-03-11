"""
SEO_MULTILINGUAL_DEFAULT_LANGUAGE

Must be in LANGUAGES
By default it's the first language defined in LANGUAGES
"""
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

languages = getattr(settings, 'LANGUAGES', ())
seo_multilingual_default_language = getattr(settings, 'SEO_MULTILINGUAL_DEFAULT_LANGUAGE', None)
if seo_multilingual_default_language:
    if seo_multilingual_default_language not in [a[0] for a in languages]:
        raise ImproperlyConfigured
else:
    seo_multilingual_default_language = languages[0][0]
SEO_MULTILINGUAL_DEFAULT_LANGUAGE = seo_multilingual_default_language