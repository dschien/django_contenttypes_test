# Create your models here.
from django.contrib.contenttypes.models import ContentType
from django.db import models


# Create your models here.
class SiteActions(models.Model):
    def get_name(self):
        return "plugin 2"
