from django.db import models

from something.models import SomethingConcrete, SomethingConcreteWithUser


class OtherData(models.Model):

    text = models.TextField()


class OtherExtendedData(SomethingConcrete):
    pass


class OtherProxy(SomethingConcrete):

    class Meta:
        proxy = True


class OtherExtendedWithUser(SomethingConcreteWithUser):
    pass