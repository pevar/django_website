#from django.db import models
#from django.test import TestCase
#
#
#class SeoContent(models.Model):
#    title = models.CharField(max_length=250, blank=True, null=True)
#    description = models.TextField(blank=True, null=True)
#
#
#class SeoMixinTests(TestCase):
#    model = SeoContent
#
#
#    def test_seo_content_have_seo_fields(self):
#        """
#        Every model extending the seo mixing have all the seo compliant fields
#        """
#        seo_title = 'seo title for my content'
#        seo_description = 'seo description for my content'
#        seo_content = SeoContent.objects.create(title=seo_title)
#
#        self.assertEqual(seo_content.seo_title, seo_title)
#        self.assertEqual(seo_content.seo_description, seo_description)
#
#
#    def test_seo_models_must_define_seo_fallback_fields_method(self):
#        """
#        Every model extending the seo mixing have all the seo compliant fields
#        """
#        seo_content = SeoContent()
#
#
#
#
#
#
