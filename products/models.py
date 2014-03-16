from django.db import models
from pleiadi.base.fields import AutoSlugField, HtmlTextField
from pleiadi.base.models import BaseModel
from pleiadi.seo.models import SeoMixin
from django.utils.translation import ugettext_lazy as _


class Brand(BaseModel, SeoMixin):
    name = models.CharField(_('name'), max_length=250, help_text=_('Name of the Brand'))
    slug = AutoSlugField(_('slug'), populate_from='name',
                         help_text=_('Semantic url (empty the field to automatically reset the value)'))
    description = HtmlTextField(_('description'))


class Family(BaseModel, SeoMixin):
    name = models.CharField(_('name'), max_length=250, help_text=_('Name of the Family'))
    slug = AutoSlugField(_('slug'), populate_from='name',
                         help_text=_('Semantic url (empty the field to automatically reset the value)'))
    description = HtmlTextField(_('description'))


class Product(BaseModel, SeoMixin):
    name = models.CharField(_('name'), max_length=250, help_text=_('Name of the Brand'))
    slug = AutoSlugField(_('slug'), populate_from='name',
                         help_text=_('Semantic url (empty the field to automatically reset the value)'))
    description = HtmlTextField(_('description'))