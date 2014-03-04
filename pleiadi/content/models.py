from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
from pleiadi.base.models import BaseModel
from pleiadi.base.fields import HtmlTextField, AutoSlugField
from modeltranslation.utils import build_localized_fieldname
from django.conf import settings
from filer.fields.image import FilerImageField


class BaseContent(BaseModel):
    """
    A base model for all the contents of the site

    slug:
    Try to strictly relate the localized_title and localized_slug.

    """
    title = models.CharField(_('title'), max_length=200, blank=False, null=False,
                             help_text=_('Title of your content'))
    slug = AutoSlugField(_('slug'), editable=True, populate_from='title', blank=True, unique=False, blank_unique=True,
                         help_text=_('Semantic url (empty the field to automatically reset the value)'))
    image = FilerImageField(blank=True, null=True,
                            help_text=_('Main image of your content'))
    description = HtmlTextField(_('description'), blank=True, null=True,
                                help_text=_('Main textual description of your content'))
    abstract = HtmlTextField(_('description'), blank=True, null=True,
                             help_text=_('Short textual description of your content'))

    class Meta:
        ordering = ['title']
        abstract = True

    def __unicode__(self):
        return u'%s' % (self.title, )

##
##    def seo_fallback_fields(self):
##        return super(BaseContent, self).seo_fallback_fields().update({
##            'seo_title': self.title,
##            'seo_description': self.description,
##        })
