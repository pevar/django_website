from django import forms
from django.contrib import admin
from news.models import News
from modeltranslation.admin import TranslationAdmin


def clean_unique(form, field, exclude_initial=True, format="The %(field)s %(value)s has already been taken."):
    value = form.cleaned_data.get(field)
    if value:
        qs = form._meta.model._default_manager.filter(**{field: value})
        if exclude_initial and form.initial:
            initial_value = form.initial.get(field)
            qs = qs.exclude(**{field: initial_value})
        if qs.count() > 0:
            raise forms.ValidationError(format % {'field': field, 'value': value})
    return value


class NewsAdminForm(forms.ModelForm):
    def clean_slug(self):
        return clean_unique(self, 'slug')


class NewsAdmin(TranslationAdmin):
    form = NewsAdminForm
    fieldsets = [
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords',),
            'classes': ('collapse',),
        }),
        (None, {
            'fields': ('title', 'slug', 'description', 'abstract')
        }),
        ('Media', {
            'fields': ('image',)
        })
    ]
    prepopulated_fields = {'slug': ('title',)}

    class Media(object):
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                'modeltranslation/css/tabbed_translation_fields.css',
            ),
        }


admin.site.register(News, NewsAdmin)