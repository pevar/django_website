from django.contrib.sites.managers import CurrentSiteManager
from django.contrib.sites.models import Site

from django.db import models
from django.utils.translation import ugettext_lazy as _
from filer.fields.image import FilerImageField
from modeltranslation.manager import MultilingualManager

from pleiadi.base.models import BaseModel
from pleiadi.base.fields import HtmlTextField, AutoSlugField
from pleiadi.seo.models import SeoMixin


class VisibleManager(MultilingualManager, CurrentSiteManager):
    """
    Return active and visible instances
    """
    def get_query_set(self):
        return super(VisibleManager, self).get_query_set().filter(active=True).filter(visible=True)


class BaseContent(SeoMixin, BaseModel):
    """
    A base model for all the contents of the site
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
    active = models.BooleanField(_('active'), help_text=_('inactive content isn\'t visible online in every language'),
                                 default=False)
    visible = models.BooleanField(_('visible'), help_text=_('handle content visibility for current language'),
                                  default=False)
    sites = models.ManyToManyField(Site, null=True, blank=True, related_name="%(app_label)s_%(class)s_related")

    objects = models.Manager()
    visible_on_site = VisibleManager()

    class Meta:
        ordering = ['title']
        abstract = True

    def __unicode__(self):
        return u'%s' % (self.title, )

    def seo_fallback_fields(self):

        seo_fallbacks = super(BaseContent, self).seo_fallback_fields()
        seo_fallbacks.update({
            'seo_title': self.title,
            'seo_description': self.description,
        })

        return seo_fallbacks
