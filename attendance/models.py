from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

class OfficeDay(models.Model):
    user = models.ForeignKey(User, verbose_name=_("Person"))
    day = models.DateField(verbose_name=_("Day"))
    paid = models.BooleanField(verbose_name=_("Paid"), default=False)
    
    def __unicode__(self):
        return '%s on %s' % (self.user, self.day)
    
    class Meta:
        unique_together = [
            ('user','day',)
        ]
        ordering = ('-day',)