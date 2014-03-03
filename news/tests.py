#from django.db import models
#from django.test import TestCase
#from news.models import News
#
#
#
#
#class SeoTests(TestCase):
#    model = News
#
#    def test_seo_context(self):
#        """
#        Every model extending the seo mixing have all the seo compliant fields
#        """
#        seo_title = 'seo title for my content'
#        seo_description = 'seo description for my content'
#        seo_content = self.model.objects.create(title=seo_title)
#
#        seo_dict = seo_content.seo()
#
#        self.assertEqual(seo_dict.get('seo_title', None), seo_title)
#        self.assertEqual(seo_dict.get('seo_description', None), seo_description)
#
#
#    def test_seo_models_must_define_seo_fallback_fields_method(self):
#        """
#        Every model extending the seo mixing have all the seo compliant fields
#        """
#        #seo_content = SeoContent()