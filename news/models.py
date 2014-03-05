from django.utils.translation import ugettext_lazy as _
from pleiadi.content.models import BaseContent


class News(BaseContent):
    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

