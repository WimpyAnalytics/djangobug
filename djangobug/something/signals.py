from django.db.models.signals import post_save
from django.dispatch import receiver

import tasks
import models

@receiver(post_save, sender=models.SomeData, dispatch_uid="d6590fc4-ce43-11e3-974d-0090f5e9fbc6")
def check(sender, **kwargs):
    if not kwargs.get('raw', False):
        data = kwargs['instance']

        if data.field1:
            tasks.add.delay(1, 1)
        else:
            tasks.add.delay(1, 2)
