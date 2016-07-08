from django.test import TestCase

# Create your tests here.
from core.tests import SiteFactory
from .models import SiteActions


class BasicTestCase(TestCase):
    def test_site_factory(self):
        a2 = SiteActions()
        a2.save()
        site = SiteFactory(name='test3', content_object=a2)
        self.assertTrue(site.content_object.get_name() == 'plugin 2')
