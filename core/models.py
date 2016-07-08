from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType


class BaseEntity(models.Model):
    class Meta:
        abstract = True

    def get_content_type(self):
        return ContentType.objects.get_for_model(self).id


# Create your models here.
class Site(BaseEntity):
    name = models.CharField(max_length=50, null=True, unique=True)

    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.name


class DefaultSiteActions(models.Model):

    def get_name(self):
        return "default"
