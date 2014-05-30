from django.test import TestCase
from django.core.cache import cache

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

    def test_something2(self):
        models.SomeData.objects.all()
        #self.fail('A failure')


class SomeTest2(TestCase):

    fixtures = ['somedatas']

    def setUp(self):
        for key in cache.iter_keys('*something*'):
            cache.delete(key)

    def test_something1(self):
        models.SomeData.objects.all()

        data = models.SomeData.objects.create(field1=False)
        data.field = True
        data.save()

    def test_something_pass(self):
        models.SomeData.objects.all()

        data = models.SomeData.objects.create(field1=False)
        data.field1 = True
        data.save()

        keys = [cache.iter_keys('*something*')]
        self.assertEquals(len(keys), 1)