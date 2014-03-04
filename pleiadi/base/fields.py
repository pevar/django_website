from django.db import models
from django.core import exceptions
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
    blank_unique = True

    def __init__(self, *args, **kwargs):
        self.populate_from = kwargs.pop('populate_from', '')
        self.blank_unique = kwargs.pop('blank_unique', '')
        super(AutoSlugField, self).__init__(*args, **kwargs)

    def validate(self, value, model_instance):
        super(AutoSlugField, self).validate(value, model_instance)

        # blank_unique
        if self.blank_unique and value not in self.empty_values:
            model = type(model_instance)

            unique_lookup = self.get_validator_unique_lookup_type()
            exist = model.objects.filter(**{unique_lookup: value}).count()

            if exist:
                raise exceptions.ValidationError(self.error_messages['unique'],
                                                 code='unique',
                                                 params={
                                                     'model_name': model,
                                                     'field_label': self.name
                                                 })

add_introspection_rules([], ["^pleiadi\.base\.fields\.AutoSlugField"])