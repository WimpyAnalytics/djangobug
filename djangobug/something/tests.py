from django.test import TestCase

import models


class SomeTest(TestCase):

    fixtures = ['somedatas']

    def test_something_fail(self):
        models.SomeData.objects.all()
        self.fail('A failure')


class SomeTest2(TestCase):

    fixtures = ['somedatas']

    def test_something_error(self):
        models.SomeData.objects.all()

        data = models.SomeData.objects.create(field1=False)
        data.field = True
        data.save1()

    def test_something_pass(self):
        models.SomeData.objects.all()

        data = models.SomeData.objects.create(field1=False)
        data.field1 = True
        data.save()