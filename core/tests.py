from django.test import TestCase

# Create your tests here.

import factory
from faker.factory import Factory as FakerFactory

from .models import Site, DefaultSiteActions

faker = FakerFactory.create()


class SiteFactory(factory.django.DjangoModelFactory):
    """
    A factory that creates a new device with 10 measuremnts
    """

    class Meta:
        model = Site

    @factory.lazy_attribute
    def content_object(self):
        a = DefaultSiteActions()
        a.save()

        return a

    name = factory.LazyAttribute(lambda o: faker.street_name())


class BasicTestCase(TestCase):
    def test_site_factory(self):
        site = SiteFactory(name='test')
        self.assertTrue(site.content_object.get_name() == 'default')
