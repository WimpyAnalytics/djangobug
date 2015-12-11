from django.test import TestCase

import models


class OtherTest(TestCase):

    fixtures = ['otherdatas']

    def test_other(self):
        models.OtherData.objects.create(text='')


class OtherExtendedTest(TestCase):

    fixtures = ['otherdatas']

    def test_other(self):
        models.OtherExtendedData.objects.create(field1=True)


class OtherProxyTest(TestCase):

    def test_other(self):
        models.OtherExtendedData.objects.create(field1=True)


class OtherConcreteWithUserTest(TestCase):

    def test_other(self):
        models.OtherExtendedWithUser.objects.create(field1=True)