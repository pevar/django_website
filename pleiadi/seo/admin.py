#from django.contrib import admin
#
#
#class SeoAdminModel(admin.ModelAdmin):
#    pass
#    #seo_fieldsets = [('SEO', {
#    #    'fields': ('seo_title', 'seo_description', 'seo_keywords',),
#    #    'classes': ('collapse',),
#    #})]
#    #
#    #def get_fieldsets(self, request, obj=None):
#    #    #fieldsets = super(SeoAdminModel, self).get_fieldsets(request, obj)
#    #    #
#    #    #fieldsets.insert(0, self.seo_fieldsets[0])
#    #
#    #    return self.seo_fieldsets
#
#
#    #def __init__(self, *args, **kwargs):
#    #    super(SeoAdminMixin, self).__init__(*args, **kwargs)
#    #
#    #    try:
#    #        self.fieldsets.insert(0, self.seo_fieldsets[0])
#    #    except AttributeError, e:
#    #        raise AttributeError('Admin Class must have fieldsets defined')