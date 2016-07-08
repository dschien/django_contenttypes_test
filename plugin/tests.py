from django.test import TestCase

# Create your tests here.
from core.tests import SiteFactory
from .models import SiteActions


class BasicTestCase(TestCase):
    def test_site_factory(self):
        a1 = SiteActions()
        a1.save()
        site = SiteFactory(name='test2', content_object=a1)
        self.assertTrue(site.content_object.get_name() == 'plugin 1')
