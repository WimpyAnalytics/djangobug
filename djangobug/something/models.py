from django.db import models
from django.conf import settings


class SomethingAbstract(models.Model):

    field1 = models.BooleanField(default=False)

    class Meta:
        abstract = True


class SomethingConcrete(SomethingAbstract):

    field2 = models.BooleanField(default=True)


class SomethingAbstractWithUser(models.Model):

    field1 = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    class Meta:
        abstract = True


class SomethingConcreteWithUser(SomethingAbstractWithUser):

    class Meta:
        abstract = True