from django.test import TestCase

import models


class SomeTest(TestCase):

    fixtures = ['somedatas']

    def test_something(self):
        models.SomeData.objects.all()


class SomeTest2(TestCase):

    fixtures = ['somedatas']

    def test_something2(self):
        models.SomeData.objects.all()

        data = models.SomeData.objects.create(field1=False)
        data.field1 = True
        data.save()