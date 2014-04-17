from django.contrib.sites.models import Site
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from modeltranslation.admin import TranslationAdmin
from django.utils.translation import ugettext_lazy as _


class BaseContentAdmin(TranslationAdmin):
    # TODO: seo fieldset should be handled by a SeoAdmin mixin
    fieldsets = [
        ('SEO', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords',),
            'classes': ('collapse',),
        }),
        (None, {
            'fields': ('title', 'slug', 'description', 'abstract')
        }),
        ('Visibility', {
            'fields': ('active', 'sites', 'visible')
        }),
        ('Media', {
            'fields': ('image',)
        })
        ,
        ('Extended', {
            'fields': (
                ('created_by', 'changed_by',),
            ),
            'classes': ('collapse',),
        })
    ]
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_by', 'changed_by',)

    class Media(object):
        js = (
            'core/tinymce/js/tinymce/tinymce.min.js',
            'core/tinymce/js/tinymce/htmltext.js',
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': (
                'modeltranslation/css/tabbed_translation_fields.css',
            ),
        }

    def get_form(self, request, obj=None, **kwargs):
        form = super(BaseContentAdmin, self).get_form(request, obj, **kwargs)

        if 'active' in form.base_fields and obj is None:
            form.base_fields['active'].initial = True

        # Changing widget and default value of site field
        if 'sites' in form.base_fields:
            form.base_fields['sites'].widget = forms.CheckboxSelectMultiple()
            form.base_fields['sites'].help_text = _('Make this content visible for selected sites according to '
                                                    'Global and Language visibility')

            # always select current site for new items
            if obj is None:
                form.base_fields['sites'].initial = [Site.objects.get_current()]

        return form

    def save_model(self, request, obj, form, change):
        #deal with owner
        created_by = None
        try:
            created_by = getattr(obj, 'created_by')
        except ObjectDoesNotExist:
            pass
        if created_by is None:
            obj.created_by = request.user

        try:
            getattr(obj, 'changed_by')
        except ObjectDoesNotExist:
            pass
        obj.changed_by = request.user

        super(BaseContentAdmin, self).save_model(request, obj, form, change)