from django.db import models
from django.utils.translation import ugettext_lazy as _


class SeoMixin(models.Model):
    """
    Implementing seo features for all the extending models
    """
    seo_title = models.CharField(_('seo title'), max_length=250, blank=True, null=True)
    seo_description = models.TextField(_('seo description'), blank=True, null=True)
    seo_keywords = models.CharField(_('seo keywords'), max_length=400, blank=True, null=True)

    class Meta:
        abstract = True

    def seo_fallback_fields(self):
        """
        Return a dict of field used as seo fallback fields.
        Override this method to supply your model specific fallback fields.
        """
        return {
            'seo_title': self.seo_title,
            'seo_description': self.seo_description,
            'seo_keywords': self.seo_keywords,
        }

    def seo(self):
        """
        Return a dict of seo fields according to the defined fallback.
        """
        fallback = self.seo_fallback_fields()

        return {
            'seo_title': self.seo_title or fallback.get('seo_title', u''),
            'seo_description': self.seo_description or fallback.get('seo_description', u''),
            'seo_keywords': self.seo_keywords or fallback.get('seo_keywords', u''),
        }