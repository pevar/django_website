from django.db import models
from pleiadi.base.fields import AutoSlugField, HtmlTextField
from pleiadi.base.models import BaseModel
from django.utils.translation import ugettext_lazy as _


class BusinessUnit(BaseModel):
    name = models.CharField(_('name'), max_length=250, help_text=_('Name of the Business Unit'))
    slug = AutoSlugField(_('slug'), help_text=_('Semantic url (empty the field to automatically reset the value)'))
    code = models.SlugField(_('code'), unique=True, help_text=_('Unique identifier of the Business Unit'))
    description = HtmlTextField(_('description'))