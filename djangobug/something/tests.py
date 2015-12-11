from django.test import TestCase
from django.core.cache import cache

import models


class SomeTest(TestCase):

    fixtures = ['somedatas']

    def setUp(self):
        pass

    def test_something2(self):
        models.SomethingConcrete.objects.all()
        #self.fail('A failure')
