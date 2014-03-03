from django.db import models
from south.modelsinspector import add_introspection_rules


class HtmlTextField(models.TextField):
    """
    Simple wrap of a standard TextField stores HtmlContent's specific information and method
    """
    pass
add_introspection_rules([], ["^pleiadi\.base\.fields\.HtmlTextField"])


class AutoSlugField(models.SlugField):
    """
    Simple wrap of a standard SlugField used to implement populate_from policy
    """
    populate_from = ''

    def __init__(self, *args, **kwargs):
        self.populate_from = kwargs.pop('populate_from', '')
        super(AutoSlugField, self).__init__(*args, **kwargs)