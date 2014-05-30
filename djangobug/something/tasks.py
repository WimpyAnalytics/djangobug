from __future__ import absolute_import

from django.core.cache import cache

from celery import shared_task
from celery.utils.log import get_task_logger

from something import models

logger = get_task_logger(__name__)

@shared_task()
def add(first, second):
    logger.info('Adding numbers {}, {}'.format(first, second))
    print first + second
    for data in models.SomeData.objects.all():
        cache.set('something.{}'.format(data.id), data, 604800)  # Expires in 7 days