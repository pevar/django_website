from modeltranslation.admin import TranslationAdmin


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
            'fields': ('active', 'visible')
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