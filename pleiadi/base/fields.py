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
    Simple wrap of a standard SlugField

    blank=True, unique=False, blank_unique=True
    This configuration allow you to save model instances with a blank slug (blank=True, unique=False) but not more than
    one instance with the same slug (blank_unique=True).

    Every validation over the field is applied to the localized version of the field.

    Eg:
    title_en -> populate -> slug_en
    the blank_unique check is made over the slug_en field values
    """
    populate_from = ''
    blank_unique = True

    def __init__(self, *args, **kwargs):
        self.populate_from = kwargs.pop('populate_from', '')
        self.blank_unique = kwargs.pop('blank_unique', True)
        kwargs['blank'] = kwargs.get('blank', True)
        kwargs['unique'] = kwargs.get('unique', False)
        super(AutoSlugField, self).__init__(*args, **kwargs)


    def validate(self, value, model_instance):
        super(AutoSlugField, self).validate(value, model_instance)

        # blank_unique
        if self.blank_unique and value not in self.empty_values:
            model = type(model_instance)
            unique_lookup = self.get_validator_unique_lookup_type()
            unique_check = model.objects.filter(**{unique_lookup: value})
            if model_instance.pk:
                unique_check = unique_check.exclude(pk=model_instance.pk)
            exist = unique_check.count()

            if exist:
                raise exceptions.ValidationError(self.error_messages['unique'],
                                                 code='unique',
                                                 params={
                                                     'model_name': model,
                                                     'field_label': self.name
                                                 })

add_introspection_rules([], ["^pleiadi\.base\.fields\.AutoSlugField"])