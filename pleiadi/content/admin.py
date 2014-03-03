#from django.contrib import admin
#from pleiadi.seo.admin import SeoAdminModel
#
#
#class BaseContentAdminClass(SeoAdminModel):
#    def get_fieldsets(self, request, obj=None):
#        fieldsets = super(BaseContentAdminClass, self).get_fieldsets(request, obj)
#        fieldsets += [
#            (None, {
#                'fields': ('title', 'slug', 'description', 'abstract')
#            }),
#            ('Media', {
#                'fields': ('image',)
#            })
#        ]
#        return fieldsets
#
#    search_fields = ('title', 'description', 'abstract')
#    list_display = ('title', 'image', 'abstract')