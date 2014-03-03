from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from modeltranslation.utils import build_localized_fieldname
from pleiadi.content.models import BaseContent


class News(BaseContent):
    seo_title = models.CharField(_('seo title'), max_length=250, blank=True, null=True)
    seo_description = models.TextField(_('seo description'), blank=True, null=True)
    seo_keywords = models.CharField(_('seo keywords'), max_length=400, blank=True, null=True)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

