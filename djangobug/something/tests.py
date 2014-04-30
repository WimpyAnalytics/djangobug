from django.test import TestCase

import models

class SomeTest(TestCase):

    fixtures = ['somedatas']

    def test_something(self):
        models.SomeData.objects.all()
