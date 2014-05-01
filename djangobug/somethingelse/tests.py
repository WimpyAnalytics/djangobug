from django.test import TestCase

import models


class OtherTest(TestCase):

    fixtures = ['otherdatas']

    def test_other(self):
        models.OtherData.objects.create(text='')