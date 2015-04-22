from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class Date(CMSPlugin):
    date = models.DateField(_('Date'))

    def __str__(self):
        return self.date.isoformat()
