from django.test import TestCase

import models


class OtherTest(TestCase):

    def test_other(self):
        models.OtherData.objects.create(text='')