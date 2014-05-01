from django.test import TestCase

import models
from zinnia.models import Category, Entry


class SomeTest(TestCase):

    fixtures = ['somedatas']

    def setUp(self):
        self.category = Category.objects.create(title='Features', slug='features')
        self.entry = Entry.objects.create(
            title='Test Entry',
            slug='test-entry',
        )
        self.entry.categories.add(self.category)

    def test_something_fail(self):
        models.SomeData.objects.all()
        #self.fail('A failure')


class SomeTest2(TestCase):

    fixtures = ['somedatas']

    def test_something_error(self):
        models.SomeData.objects.all()

        data = models.SomeData.objects.create(field1=False)
        data.field = True
        #data.save1()

    def test_something_pass(self):
        models.SomeData.objects.all()

        data = models.SomeData.objects.create(field1=False)
        data.field1 = True
        data.save()