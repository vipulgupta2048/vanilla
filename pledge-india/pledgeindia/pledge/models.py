from django.db import models
from django.utils.translation import ugettext_lazy as _
from user.models import User
from base.models import TimeStampedModel


# Create your models here.
class Pledge(TimeStampedModel):
    """Pledge Model"""

    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'), null=True)

    class Meta:
        verbose_name = _('pledge')
        verbose_name_plural = _('pledges')

    def __str__(self):
        return self.title


class UserPledges(TimeStampedModel):
    """User Pledges Model"""

    pledge = models.ForeignKey(Pledge, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    taken_on = models.DateTimeField(
        _('taken on'), auto_now_add=True, help_text="Datetime at which user took the pledge")

    def __str__(self):
        return "%s by %s" % (self.pledge.title, self.user.first_name)
