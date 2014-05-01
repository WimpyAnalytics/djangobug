from __future__ import absolute_import

from celery import shared_task

from something import models

@shared_task()
def add(first, second):
    print first + second
    for data in models.SomeData.objects.all():
        print data