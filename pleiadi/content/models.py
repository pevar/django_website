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

#    def save(self, *args, **kwargs):
#        """
#        We want that, when saving a model, the AutoSlugField populate_from refer to the right language
#
#        Eg:
#        slug_en -> populated from -> title_en
#        slug_it -> populated from -> title_it
#        ecc...
#
#        If the content is not translated in a particular language the slug will be blank
#        TODO: find a way to force blank=True and remove blank from the available parameters of the AutoSlugField
#
#        Eg:
#        title_it = blank -> slug_it = blank
#
#        This scenario is not allowed for a standard unique kind of field
#        """
#        destination_field_name = 'slug'
#        for field in self._meta.fields:
#            if field.name == destination_field_name:
#                source_field_name = getattr(field, 'populate_from', '')
#                break
#
#        for lang_code, lang_verbose in settings.LANGUAGES:
#            local_destination_field_name = build_localized_fieldname(destination_field_name, lang_code)
#            local_source_field_name = build_localized_fieldname(source_field_name, lang_code)
#
#            if hasattr(self, local_destination_field_name) and not getattr(self, local_destination_field_name):
#                # localized slug field is not set
#
#                if hasattr(self, local_source_field_name) and getattr(self, local_source_field_name):
#                    # localized populate_from field is set, so I use it to populate the localized version of the
#                    # destination field
#                    setattr(self, local_destination_field_name, slugify(getattr(self, local_source_field_name)))
#
#                elif hasattr(self, source_field_name) and getattr(self, source_field_name):
#                    # localized populate_from field is not set so I use the default language (which is the first in the
#                    # LANGUAGES tuple) to populate it
#                    setattr(self, local_destination_field_name, slugify(getattr(self, source_field_name)))
#
#        super(BaseContent, self).save(*args, **kwargs)
##
##    def seo_fallback_fields(self):
##        return super(BaseContent, self).seo_fallback_fields().update({
##            'seo_title': self.title,
##            'seo_description': self.description,
##        })
